// revised-sim.mjs -- discrete occasion simulation for the revised OVMG core.
//
// The simulator samples a finite population's inclusion vectors, generates
// normalized gated choices at discrete niche occasions, routes target tokens
// and omissions into effective evidence, and applies the baseline-preserving
// update. It demonstrates inferential regimes under stated assumptions; it is
// not a proof of a stationary population dynamic or an empirical fit.

import {
  gatedChoiceProbabilities,
  makeEvidenceState,
  omissionEvidenceFromChoice,
  summary,
  updateEvidence,
} from './revised-engine.mjs';

export function mulberry32(seed) {
  let state = seed >>> 0;
  return function random() {
    state = (state + 0x6d2b79f5) >>> 0;
    let value = state;
    value = Math.imul(value ^ (value >>> 15), value | 1);
    value ^= value + Math.imul(value ^ (value >>> 7), value | 61);
    return ((value ^ (value >>> 14)) >>> 0) / 4294967296;
  };
}

function requireProbability(value, name) {
  if (!Number.isFinite(value) || value < 0 || value > 1) {
    throw new RangeError(`${name} must be in [0, 1], got ${value}`);
  }
}

function drawBernoulli(probability, random) {
  return random() < probability;
}

function sampleOutcome(probabilities, random) {
  let draw = random();
  for (let index = 0; index < probabilities.candidates.length; index += 1) {
    draw -= probabilities.candidates[index];
    if (draw <= 0) return index;
  }
  return 'outside';
}

function opportunityCount(schedule, step) {
  const value = typeof schedule === 'function' ? schedule(step) : schedule;
  if (!Number.isInteger(value) || value < 0) {
    throw new RangeError(`opportunities at step ${step} must be a non-negative integer, got ${value}`);
  }
  return value;
}

function validateAssemblyNodeIndices(assemblyNodeIndices, nodeCount) {
  if (!Array.isArray(assemblyNodeIndices) || assemblyNodeIndices.length === 0) {
    throw new RangeError('assemblyNodeIndices must be a non-empty array');
  }
  const seen = new Set();
  assemblyNodeIndices.forEach((index) => {
    if (!Number.isInteger(index) || index < 0 || index >= nodeCount) {
      throw new RangeError(`assembly node index must be in [0, ${nodeCount}), got ${index}`);
    }
    if (seen.has(index)) throw new RangeError(`assembly node index ${index} occurs twice`);
    seen.add(index);
  });
}

function validateLectModel(lectModel, nodeCount) {
  if (lectModel === null || typeof lectModel !== 'object') {
    throw new TypeError('lectModel must be an object');
  }
  const { weights, nodeRates } = lectModel;
  if (!Array.isArray(weights) || !Array.isArray(nodeRates) || weights.length === 0) {
    throw new TypeError('lectModel requires non-empty weights and nodeRates arrays');
  }
  if (weights.length !== nodeRates.length) {
    throw new RangeError('lectModel weights and nodeRates must have the same length');
  }
  let totalWeight = 0;
  weights.forEach((weight, lectIndex) => {
    requireProbability(weight, `lectModel.weights[${lectIndex}]`);
    totalWeight += weight;
  });
  if (Math.abs(totalWeight - 1) > 1e-12) {
    throw new RangeError(`lectModel weights must sum to 1, got ${totalWeight}`);
  }
  nodeRates.forEach((rates, lectIndex) => {
    if (!Array.isArray(rates) || rates.length !== nodeCount) {
      throw new RangeError(`lectModel.nodeRates[${lectIndex}] must have ${nodeCount} entries`);
    }
    rates.forEach((rate, nodeIndex) => {
      requireProbability(rate, `lectModel.nodeRates[${lectIndex}][${nodeIndex}]`);
    });
  });
}

function defaultCandidateNodeIndices(candidateCount) {
  return Array.from({ length: candidateCount }, (_, candidateIndex) => [candidateIndex]);
}

function validateCandidateNodeIndices(candidateNodeIndices, candidateCount, nodeCount) {
  if (!Array.isArray(candidateNodeIndices) || candidateNodeIndices.length !== candidateCount) {
    throw new RangeError(`candidateNodeIndices must have ${candidateCount} entries`);
  }
  candidateNodeIndices.forEach((nodeIndices, candidateIndex) => {
    try {
      validateAssemblyNodeIndices(nodeIndices, nodeCount);
    } catch (error) {
      throw new RangeError(`candidateNodeIndices[${candidateIndex}] is invalid: ${error.message}`);
    }
  });
}

/** Candidate availability is conjunction over the construction nodes it needs. */
export function candidateAvailabilityFromNodes(nodeInclusion, candidateNodeIndices) {
  return candidateNodeIndices.map((nodeIndices) => (
    nodeIndices.every((nodeIndex) => nodeInclusion[nodeIndex])
  ));
}

function sampleIndex(weights, random) {
  let draw = random();
  for (let index = 0; index < weights.length; index += 1) {
    draw -= weights[index];
    if (draw <= 0) return index;
  }
  return weights.length - 1;
}

/** Marginal node rates induced by a latent-lect mixture. */
export function marginalNodeRates(lectModel) {
  const nodeCount = lectModel?.nodeRates?.[0]?.length;
  validateLectModel(lectModel, nodeCount);
  return Array.from({ length: nodeCount }, (_, nodeIndex) => (
    lectModel.weights.reduce((total, weight, lectIndex) => (
      total + weight * lectModel.nodeRates[lectIndex][nodeIndex]
    ), 0)
  ));
}

/**
 * Probability that a randomly drawn speaker licenses every node in an
 * assembly. Conditional node independence is assumed within each lect; the
 * mixture over lects creates the within-speaker dependence that marginals lose.
 */
export function assemblyPrevalenceFromLects(lectModel, assemblyNodeIndices) {
  const nodeCount = lectModel?.nodeRates?.[0]?.length;
  validateLectModel(lectModel, nodeCount);
  validateAssemblyNodeIndices(assemblyNodeIndices, nodeCount);
  return lectModel.weights.reduce((total, weight, lectIndex) => {
    const withinLect = assemblyNodeIndices.reduce((product, nodeIndex) => (
      product * lectModel.nodeRates[lectIndex][nodeIndex]
    ), 1);
    return total + weight * withinLect;
  }, 0);
}

/** The incorrect independent-marginal approximation, exposed for diagnostics. */
export function independentMarginalAssemblyPrevalence(lectModel, assemblyNodeIndices) {
  const rates = marginalNodeRates(lectModel);
  validateAssemblyNodeIndices(assemblyNodeIndices, rates.length);
  return assemblyNodeIndices.reduce((product, nodeIndex) => product * rates[nodeIndex], 1);
}

function makePopulation({ speakerCount, trueRates, lectModel, random }) {
  if (lectModel) {
    const population = [];
    const lectAssignments = [];
    for (let speakerIndex = 0; speakerIndex < speakerCount; speakerIndex += 1) {
      const lectIndex = sampleIndex(lectModel.weights, random);
      lectAssignments.push(lectIndex);
      population.push(lectModel.nodeRates[lectIndex].map((rate) => drawBernoulli(rate, random)));
    }
    return { population, lectAssignments };
  }
  return {
    population: Array.from({ length: speakerCount }, () => (
      trueRates.map((rate) => drawBernoulli(rate, random))
    )),
    lectAssignments: null,
  };
}

function observedCandidatePrevalence(population, candidateNodeIndices) {
  return observedAssemblyPrevalence(population, candidateNodeIndices);
}

function observedAssemblyPrevalence(population, assemblyNodeIndices) {
  const licensed = population.reduce((count, availability) => (
    count + Number(assemblyNodeIndices.every((nodeIndex) => availability[nodeIndex]))
  ), 0);
  return licensed / population.length;
}

/**
 * Simulate evidence for one target candidate in one fixed population. A
 * population may use independent node rates or a latent-lect mixture. The
 * target's posterior is updated; candidate availability is derived from the
 * construction nodes each candidate needs. Other candidates shape the
 * gated-choice likelihood and an optional multi-node assembly prevalence is
 * reported.
 */
export function simulateEvidenceRegime(params = {}, steps = 80, seed = 1) {
  const {
    utilities = [0, 0],
    trueRates = [0, 1],
    targetIndex = 0,
    outsideUtility = 0,
    speakerCount = 200,
    opportunitiesPerStep = 8,
    priorA = 1,
    priorB = 1,
    deltaM = 1,
    lambdaPos = 1,
    lambdaNeg = 1,
    recoverability = 1,
    lectModel = null,
    assemblyNodeIndices = null,
    candidateNodeIndices = null,
  } = params;
  if (!Array.isArray(utilities) || utilities.length === 0) {
    throw new RangeError('utilities must be a non-empty array');
  }
  if (!Number.isInteger(targetIndex) || targetIndex < 0 || targetIndex >= utilities.length) {
    throw new RangeError(`targetIndex must identify a candidate, got ${targetIndex}`);
  }
  if (!Number.isInteger(speakerCount) || speakerCount <= 0) {
    throw new RangeError(`speakerCount must be a positive integer, got ${speakerCount}`);
  }
  if (!Number.isInteger(steps) || steps < 0) {
    throw new RangeError(`steps must be a non-negative integer, got ${steps}`);
  }
  const nodeCount = lectModel
    ? lectModel?.nodeRates?.[0]?.length
    : Array.isArray(trueRates) ? trueRates.length : undefined;
  if (!Number.isInteger(nodeCount) || nodeCount <= 0) {
    throw new RangeError('trueRates or lectModel.nodeRates must specify at least one construction node');
  }
  if (lectModel) validateLectModel(lectModel, nodeCount);
  else {
    if (!Array.isArray(trueRates) || trueRates.length !== nodeCount) {
      throw new RangeError('trueRates must be a non-empty node-rate array');
    }
    trueRates.forEach((rate, index) => requireProbability(rate, `trueRates[${index}]`));
  }
  requireProbability(recoverability, 'recoverability');
  const candidateNodes = candidateNodeIndices ?? defaultCandidateNodeIndices(utilities.length);
  validateCandidateNodeIndices(candidateNodes, utilities.length, nodeCount);
  const assemblyNodes = assemblyNodeIndices ?? candidateNodes[targetIndex];
  validateAssemblyNodeIndices(assemblyNodes, nodeCount);

  const random = mulberry32(seed);
  const { population, lectAssignments } = makePopulation({
    speakerCount,
    trueRates,
    lectModel,
    random,
  });
  const theoreticalAssemblyPrevalence = lectModel
    ? assemblyPrevalenceFromLects(lectModel, assemblyNodes)
    : assemblyNodes.reduce((product, nodeIndex) => product * trueRates[nodeIndex], 1);
  const theoreticalTargetPrevalence = lectModel
    ? assemblyPrevalenceFromLects(lectModel, candidateNodes[targetIndex])
    : candidateNodes[targetIndex].reduce((product, nodeIndex) => product * trueRates[nodeIndex], 1);
  let state = makeEvidenceState({ priorA, priorB });
  const rows = [{
    step: 0,
    opportunities: 0,
    targetTokens: 0,
    omissions: 0,
    positiveEvidence: 0,
    negativeEvidence: 0,
    targetPopulationPrevalence: observedCandidatePrevalence(population, candidateNodes[targetIndex]),
    assemblyPopulationPrevalence: observedAssemblyPrevalence(population, assemblyNodes),
    theoreticalAssemblyPrevalence,
    theoreticalTargetPrevalence,
    ...summary(state),
  }];

  for (let step = 1; step <= steps; step += 1) {
    const opportunities = opportunityCount(opportunitiesPerStep, step);
    let positiveEvidence = 0;
    let negativeEvidence = 0;
    let targetTokens = 0;
    let omissions = 0;
    for (let occasion = 0; occasion < opportunities; occasion += 1) {
      const speakerIndex = Math.floor(random() * speakerCount);
      const nodeInclusion = population[speakerIndex];
      const availability = candidateAvailabilityFromNodes(nodeInclusion, candidateNodes);
      const probabilities = gatedChoiceProbabilities({ utilities, availability, outsideUtility });
      const outcome = sampleOutcome(probabilities, random);
      if (outcome === targetIndex) {
        targetTokens += 1;
        positiveEvidence += 1;
        continue;
      }
      omissions += 1;
      const evidence = omissionEvidenceFromChoice({
        utilities,
        availability,
        targetIndex,
        observedOutcome: outcome,
        outsideUtility,
        recoverability,
      });
      positiveEvidence += evidence.positive;
      negativeEvidence += evidence.negative;
    }
    state = updateEvidence(
      state,
      { positive: positiveEvidence, negative: negativeEvidence },
      { deltaM, lambdaPos, lambdaNeg },
    );
    rows.push({
      step,
      opportunities,
      targetTokens,
      omissions,
      positiveEvidence,
      negativeEvidence,
      targetPopulationPrevalence: observedCandidatePrevalence(population, candidateNodes[targetIndex]),
      assemblyPopulationPrevalence: observedAssemblyPrevalence(population, assemblyNodes),
      theoreticalAssemblyPrevalence,
      theoreticalTargetPrevalence,
      ...summary(state),
    });
  }

  return { rows, population, lectAssignments };
}

/**
 * Regimes used by the test suite. Winnerlessness is conditional on a low
 * analogical prior plus outside-option evidence starvation; it is not obtained
 * from no evidence alone.
 */
export const REVISED_REGIMES = Object.freeze({
  licensed: {
    utilities: [4, 0],
    trueRates: [1, 1],
    outsideUtility: -4,
    opportunitiesPerStep: 8,
    priorA: 1,
    priorB: 1,
  },
  preempted: {
    utilities: [0, 0],
    trueRates: [0, 1],
    outsideUtility: -5,
    opportunitiesPerStep: 8,
    priorA: 1,
    priorB: 1,
  },
  starved: {
    utilities: [0, 0],
    trueRates: [0, 1],
    outsideUtility: -5,
    opportunitiesPerStep: 0,
    priorA: 1,
    priorB: 1,
  },
  winnerless: {
    utilities: [-7, -7],
    trueRates: [0, 0],
    outsideUtility: 0,
    opportunitiesPerStep: 8,
    priorA: 0.25,
    priorB: 3.75,
  },
});
