// joint-likelihood.mjs -- small executable likelihood contract for OVMG v2.
//
// This evaluator composes the channels named in the paper: latent lect and
// node inclusion, situation/cues, gated production, repair, ratings, and
// confidence. It is intentionally small. Exact marginalization over a
// speaker's inclusion vector is exponential in node count and therefore a
// validation tool for toy cases, not a replacement for Stan/PyMC inference.
//
// The discounted effective-evidence update is not counted as a second data
// likelihood here. It is a transparent learner-state emulator. A full fit can
// use it as a tempered state approximation or replace it with a state-space
// posterior derived from this generative model.

import { gatedChoiceProbabilities, outcomeProbability } from './revised-engine.mjs';

const LOG_ZERO = -Infinity;

function requireFinite(value, name) {
  if (!Number.isFinite(value)) throw new TypeError(`${name} must be finite, got ${value}`);
}

function requireProbability(value, name) {
  requireFinite(value, name);
  if (value < 0 || value > 1) {
    throw new RangeError(`${name} must be in [0, 1], got ${value}`);
  }
}

function logProbability(probability) {
  requireProbability(probability, 'probability');
  return probability === 0 ? LOG_ZERO : Math.log(probability);
}

function logBernoulli(observed, probability) {
  if (typeof observed !== 'boolean') throw new TypeError(`Bernoulli observation must be boolean, got ${observed}`);
  return logProbability(observed ? probability : 1 - probability);
}

function logistic(value) {
  if (value >= 0) {
    const inverse = Math.exp(-value);
    return 1 / (1 + inverse);
  }
  const direct = Math.exp(value);
  return direct / (1 + direct);
}

function logSumExp(values) {
  const maximum = Math.max(...values);
  if (maximum === LOG_ZERO) return LOG_ZERO;
  const sum = values.reduce((total, value) => total + Math.exp(value - maximum), 0);
  return maximum + Math.log(sum);
}

function validateCutpoints(cutpoints, name) {
  if (!Array.isArray(cutpoints) || cutpoints.length === 0) {
    throw new TypeError(`${name}.cutpoints must be a non-empty array`);
  }
  cutpoints.forEach((cutpoint, index) => {
    requireFinite(cutpoint, `${name}.cutpoints[${index}]`);
    if (index > 0 && !(cutpoint > cutpoints[index - 1])) {
      throw new RangeError(`${name}.cutpoints must be strictly increasing`);
    }
  });
}

/** Ordered-logit log probability for zero-indexed categories. */
export function orderedLogitLogProbability(category, location, cutpoints) {
  if (!Number.isInteger(category) || category < 0 || category > cutpoints.length) {
    throw new RangeError(`category must be in [0, ${cutpoints.length}], got ${category}`);
  }
  requireFinite(location, 'location');
  validateCutpoints(cutpoints, 'ordered logit');
  const lower = category === 0 ? 0 : logistic(cutpoints[category - 1] - location);
  const upper = category === cutpoints.length ? 1 : logistic(cutpoints[category] - location);
  return Math.log(Math.max(upper - lower, Number.MIN_VALUE));
}

/** Bounded anomaly signal F from the current paper's read-out structure. */
export function anomalySignal({
  statusEstimate,
  processingCost = 0,
  plausibilityCost = 0,
  prescriptiveDissonance = 0,
  alpha = 1,
  processingWeight = 1,
  plausibilityWeight = 1,
  dissonanceWeight = 1,
}) {
  requireProbability(statusEstimate, 'statusEstimate');
  [
    [processingCost, 'processingCost'],
    [plausibilityCost, 'plausibilityCost'],
    [prescriptiveDissonance, 'prescriptiveDissonance'],
    [alpha, 'alpha'],
    [processingWeight, 'processingWeight'],
    [plausibilityWeight, 'plausibilityWeight'],
    [dissonanceWeight, 'dissonanceWeight'],
  ].forEach(([value, name]) => requireFinite(value, name));
  const anomalyDrive = alpha * (1 - statusEstimate) +
    processingWeight * processingCost +
    plausibilityWeight * plausibilityCost +
    dissonanceWeight * prescriptiveDissonance;
  const nonnegativeDrive = Math.max(anomalyDrive, 0);
  return -nonnegativeDrive / (1 + nonnegativeDrive);
}

function defaultCandidateNodeIndices(candidateCount) {
  return Array.from({ length: candidateCount }, (_, candidateIndex) => [candidateIndex]);
}

function validateCandidateNodeIndices(candidateNodeIndices, candidateCount, nodeCount) {
  if (!Array.isArray(candidateNodeIndices) || candidateNodeIndices.length !== candidateCount) {
    throw new RangeError(`candidateNodeIndices must have ${candidateCount} entries`);
  }
  candidateNodeIndices.forEach((nodeIndices, candidateIndex) => {
    if (!Array.isArray(nodeIndices) || nodeIndices.length === 0) {
      throw new RangeError(`candidateNodeIndices[${candidateIndex}] must be a non-empty array`);
    }
    const seen = new Set();
    nodeIndices.forEach((nodeIndex) => {
      if (!Number.isInteger(nodeIndex) || nodeIndex < 0 || nodeIndex >= nodeCount) {
        throw new RangeError(`candidateNodeIndices[${candidateIndex}] contains invalid node ${nodeIndex}`);
      }
      if (seen.has(nodeIndex)) {
        throw new RangeError(`candidateNodeIndices[${candidateIndex}] repeats node ${nodeIndex}`);
      }
      seen.add(nodeIndex);
    });
  });
}

function candidateAvailabilityFromInclusion(inclusion, candidateNodeIndices) {
  return candidateNodeIndices.map((nodeIndices) => (
    nodeIndices.every((nodeIndex) => inclusion[nodeIndex])
  ));
}

function validateModel(model) {
  if (!model || typeof model !== 'object') throw new TypeError('model must be an object');
  const { lectWeights, nodeRates, utilitiesByContext, outsideUtilitiesByContext, contextPrior } = model;
  if (!Array.isArray(lectWeights) || !Array.isArray(nodeRates) || lectWeights.length === 0) {
    throw new TypeError('model requires non-empty lectWeights and nodeRates arrays');
  }
  if (lectWeights.length !== nodeRates.length) {
    throw new RangeError('lectWeights and nodeRates must have the same length');
  }
  const nodeCount = nodeRates[0]?.length;
  if (!Number.isInteger(nodeCount) || nodeCount <= 0) {
    throw new RangeError('nodeRates must contain at least one construction-node rate');
  }
  let totalLectWeight = 0;
  lectWeights.forEach((weight, lectIndex) => {
    requireProbability(weight, `lectWeights[${lectIndex}]`);
    totalLectWeight += weight;
  });
  if (Math.abs(totalLectWeight - 1) > 1e-12) {
    throw new RangeError(`lectWeights must sum to 1, got ${totalLectWeight}`);
  }
  nodeRates.forEach((rates, lectIndex) => {
    if (!Array.isArray(rates) || rates.length !== nodeCount) {
      throw new RangeError(`nodeRates[${lectIndex}] must have ${nodeCount} entries`);
    }
    rates.forEach((rate, nodeIndex) => requireProbability(rate, `nodeRates[${lectIndex}][${nodeIndex}]`));
  });
  if (!Array.isArray(contextPrior) || !Array.isArray(utilitiesByContext) ||
    !Array.isArray(outsideUtilitiesByContext) || contextPrior.length === 0) {
    throw new TypeError('model requires contextPrior, utilitiesByContext, and outsideUtilitiesByContext arrays');
  }
  if (contextPrior.length !== utilitiesByContext.length ||
    contextPrior.length !== outsideUtilitiesByContext.length) {
    throw new RangeError('context arrays must have the same length');
  }
  const candidateCount = utilitiesByContext[0]?.length;
  if (!Number.isInteger(candidateCount) || candidateCount <= 0) {
    throw new RangeError('utilitiesByContext must contain at least one candidate utility');
  }
  let totalContextWeight = 0;
  contextPrior.forEach((weight, contextIndex) => {
    requireProbability(weight, `contextPrior[${contextIndex}]`);
    totalContextWeight += weight;
    const utilities = utilitiesByContext[contextIndex];
    if (!Array.isArray(utilities) || utilities.length !== candidateCount) {
      throw new RangeError(`utilitiesByContext[${contextIndex}] must have ${candidateCount} entries`);
    }
    utilities.forEach((utility, candidateIndex) => (
      requireFinite(utility, `utilitiesByContext[${contextIndex}][${candidateIndex}]`)
    ));
    requireFinite(outsideUtilitiesByContext[contextIndex], `outsideUtilitiesByContext[${contextIndex}]`);
  });
  if (Math.abs(totalContextWeight - 1) > 1e-12) {
    throw new RangeError(`contextPrior must sum to 1, got ${totalContextWeight}`);
  }
  const candidateNodeIndices = model.candidateNodeIndices ?? defaultCandidateNodeIndices(candidateCount);
  validateCandidateNodeIndices(candidateNodeIndices, candidateCount, nodeCount);
  if (model.cueLikelihoods !== undefined) {
    if (!Array.isArray(model.cueLikelihoods) || model.cueLikelihoods.length !== contextPrior.length) {
      throw new RangeError('cueLikelihoods must have one row per context');
    }
    model.cueLikelihoods.forEach((likelihoods, contextIndex) => {
      if (!Array.isArray(likelihoods) || likelihoods.length === 0) {
        throw new TypeError(`cueLikelihoods[${contextIndex}] must be a non-empty array`);
      }
      const total = likelihoods.reduce((sum, value, cueIndex) => {
        requireProbability(value, `cueLikelihoods[${contextIndex}][${cueIndex}]`);
        return sum + value;
      }, 0);
      if (Math.abs(total - 1) > 1e-12) {
        throw new RangeError(`cueLikelihoods[${contextIndex}] must sum to 1, got ${total}`);
      }
    });
  }
  return { nodeCount, candidateCount, candidateNodeIndices, contextCount: contextPrior.length };
}

/** Derive q(c | cue) from a situation prior and a generative cue likelihood. */
export function contextPosteriorFromCue({ contextPrior, cueLikelihoods, cue }) {
  if (!Array.isArray(contextPrior) || !Array.isArray(cueLikelihoods) ||
    contextPrior.length === 0 || contextPrior.length !== cueLikelihoods.length) {
    throw new TypeError('contextPrior and cueLikelihoods must be same-length non-empty arrays');
  }
  if (!Number.isInteger(cue) || cue < 0) throw new RangeError(`cue must be a non-negative integer, got ${cue}`);
  let priorTotal = 0;
  const unnormalized = contextPrior.map((prior, contextIndex) => {
    requireProbability(prior, `contextPrior[${contextIndex}]`);
    priorTotal += prior;
    const likelihoods = cueLikelihoods[contextIndex];
    if (!Array.isArray(likelihoods) || cue >= likelihoods.length) {
      throw new RangeError(`cue ${cue} is invalid for context ${contextIndex}`);
    }
    let likelihoodTotal = 0;
    likelihoods.forEach((value, cueIndex) => {
      requireProbability(value, `cueLikelihoods[${contextIndex}][${cueIndex}]`);
      likelihoodTotal += value;
    });
    if (Math.abs(likelihoodTotal - 1) > 1e-12) {
      throw new RangeError(`cueLikelihoods[${contextIndex}] must sum to 1, got ${likelihoodTotal}`);
    }
    return prior * likelihoods[cue];
  });
  if (Math.abs(priorTotal - 1) > 1e-12) {
    throw new RangeError(`contextPrior must sum to 1, got ${priorTotal}`);
  }
  const normalizer = unnormalized.reduce((total, value) => total + value, 0);
  if (normalizer === 0) throw new RangeError('cue has zero probability in every context');
  return unnormalized.map((value) => value / normalizer);
}

function validateSpeaker(speaker, nodeCount, lectCount) {
  if (!speaker || typeof speaker !== 'object') throw new TypeError('speaker must be an object');
  const { lectIndex, inclusion } = speaker;
  if (!Number.isInteger(lectIndex) || lectIndex < 0 || lectIndex >= lectCount) {
    throw new RangeError(`speaker.lectIndex is invalid: ${lectIndex}`);
  }
  if (!Array.isArray(inclusion) || inclusion.length !== nodeCount) {
    throw new RangeError(`speaker.inclusion must have ${nodeCount} booleans`);
  }
  inclusion.forEach((value, index) => {
    if (typeof value !== 'boolean') throw new TypeError(`speaker.inclusion[${index}] must be boolean`);
  });
}

function readoutLogLikelihood(model, observation) {
  if (observation.rating === undefined && observation.confidenceRating === undefined) return {
    rating: 0,
    confidence: 0,
  };
  if (!observation.readout || typeof observation.readout !== 'object') {
    throw new TypeError('rating or confidence observations require observation.readout');
  }
  const {
    statusEstimate,
    decisionConfidence,
    evidenceConfidence = decisionConfidence,
    processingCost = 0,
    plausibilityCost = 0,
    prescriptiveDissonance = 0,
  } = observation.readout;
  requireProbability(statusEstimate, 'readout.statusEstimate');
  requireProbability(decisionConfidence, 'readout.decisionConfidence');
  requireProbability(evidenceConfidence, 'readout.evidenceConfidence');
  const signal = anomalySignal({
    statusEstimate,
    processingCost,
    plausibilityCost,
    prescriptiveDissonance,
    ...(model.readout ?? {}),
  });
  let rating = 0;
  let confidence = 0;
  if (observation.rating !== undefined) {
    if (!model.rating) throw new TypeError('rating observation requires model.rating');
    const { intercept = 0, anomalyWeight = 1, decisionConfidenceWeight = 0, cutpoints } = model.rating;
    [intercept, anomalyWeight, decisionConfidenceWeight].forEach((value, index) => (
      requireFinite(value, `rating coefficient ${index}`)
    ));
    rating = orderedLogitLogProbability(
      observation.rating,
      intercept + anomalyWeight * signal + decisionConfidenceWeight * decisionConfidence,
      cutpoints,
    );
  }
  if (observation.confidenceRating !== undefined) {
    if (!model.confidence) throw new TypeError('confidence observation requires model.confidence');
    const { intercept = 0, evidenceWeight = 1, decisionWeight = 0, cutpoints } = model.confidence;
    [intercept, evidenceWeight, decisionWeight].forEach((value, index) => (
      requireFinite(value, `confidence coefficient ${index}`)
    ));
    confidence = orderedLogitLogProbability(
      observation.confidenceRating,
      intercept + evidenceWeight * evidenceConfidence + decisionWeight * decisionConfidence,
      cutpoints,
    );
  }
  return { rating, confidence };
}

function repairLogLikelihood(model, observation) {
  if (observation.repair === undefined) return 0;
  if (!model.repair) throw new TypeError('repair observation requires model.repair');
  const {
    intercept = 0,
    misSetWeight = 0,
    divergenceWeight = 0,
    dissonanceWeight = 0,
  } = model.repair;
  const {
    misSet = false,
    divergence = 0,
    footing = 1,
    prescriptiveDissonance = 0,
  } = observation;
  [intercept, misSetWeight, divergenceWeight, dissonanceWeight, divergence, footing, prescriptiveDissonance]
    .forEach((value, index) => requireFinite(value, `repair value ${index}`));
  if (typeof misSet !== 'boolean' || footing < 0 || divergence < 0) {
    throw new RangeError('misSet must be boolean and divergence/footing must be non-negative');
  }
  const misSetFactor = Number(misSet);
  const probability = logistic(
    intercept + misSetFactor * (misSetWeight + divergenceWeight * divergence * footing) +
    dissonanceWeight * prescriptiveDissonance,
  );
  return logBernoulli(observation.repair, probability);
}

function observationLogLikelihood(model, speaker, observation, metadata) {
  const { contextCount, candidateNodeIndices } = metadata;
  if (!observation || typeof observation !== 'object') throw new TypeError('observation must be an object');
  const { context, outcome, cue } = observation;
  if (!Number.isInteger(context) || context < 0 || context >= contextCount) {
    throw new RangeError(`observation.context is invalid: ${context}`);
  }
  let cueLikelihood = 0;
  if (cue !== undefined) {
    if (!model.cueLikelihoods) throw new TypeError('cue observation requires model.cueLikelihoods');
    if (!Number.isInteger(cue) || cue < 0 || cue >= model.cueLikelihoods[context].length) {
      throw new RangeError(`observation.cue is invalid: ${cue}`);
    }
    cueLikelihood = logProbability(model.cueLikelihoods[context][cue]);
  }
  const probabilities = gatedChoiceProbabilities({
    utilities: model.utilitiesByContext[context],
    availability: candidateAvailabilityFromInclusion(speaker.inclusion, candidateNodeIndices),
    outsideUtility: model.outsideUtilitiesByContext[context],
  });
  const production = logProbability(outcomeProbability(probabilities, outcome));
  const repair = repairLogLikelihood(model, observation);
  const readout = readoutLogLikelihood(model, observation);
  return {
    context: logProbability(model.contextPrior[context]),
    cue: cueLikelihood,
    production,
    repair,
    rating: readout.rating,
    confidence: readout.confidence,
  };
}

/**
 * Conditional joint log likelihood for a known speaker lect, inclusion vector,
 * and situation assignment. The component return value makes accidental
 * double-counting of repair or read-out evidence inspectable in tests.
 */
export function conditionalSpeakerLogJoint({ model, speaker, observations }) {
  const metadata = validateModel(model);
  validateSpeaker(speaker, metadata.nodeCount, model.lectWeights.length);
  if (!Array.isArray(observations)) throw new TypeError('observations must be an array');
  const components = {
    lect: logProbability(model.lectWeights[speaker.lectIndex]),
    inclusion: 0,
    context: 0,
    cue: 0,
    production: 0,
    repair: 0,
    rating: 0,
    confidence: 0,
  };
  speaker.inclusion.forEach((included, nodeIndex) => {
    components.inclusion += logBernoulli(included, model.nodeRates[speaker.lectIndex][nodeIndex]);
  });
  observations.forEach((observation) => {
    const observationComponents = observationLogLikelihood(model, speaker, observation, metadata);
    Object.entries(observationComponents).forEach(([name, value]) => {
      components[name] += value;
    });
  });
  return {
    logLikelihood: Object.values(components).reduce((total, value) => total + value, 0),
    components,
  };
}

function inclusionVector(index, nodeCount) {
  return Array.from({ length: nodeCount }, (_, nodeIndex) => (
    Boolean(index & (1 << nodeIndex))
  ));
}

/**
 * Exact marginalization over a single speaker's lect and inclusion vector.
 * Contexts remain observed in this toy evaluator. The cost is O(L * 2^N), so
 * use this only for validation or tiny demonstration models.
 */
export function marginalSpeakerLogLikelihood({ model, observations }) {
  const metadata = validateModel(model);
  if (metadata.nodeCount > 20) {
    throw new RangeError('exact marginalization is limited to 20 construction nodes');
  }
  const terms = [];
  for (let lectIndex = 0; lectIndex < model.lectWeights.length; lectIndex += 1) {
    for (let index = 0; index < 2 ** metadata.nodeCount; index += 1) {
      terms.push(conditionalSpeakerLogJoint({
        model,
        speaker: { lectIndex, inclusion: inclusionVector(index, metadata.nodeCount) },
        observations,
      }).logLikelihood);
    }
  }
  return {
    logLikelihood: logSumExp(terms),
    evaluatedStates: terms.length,
  };
}
