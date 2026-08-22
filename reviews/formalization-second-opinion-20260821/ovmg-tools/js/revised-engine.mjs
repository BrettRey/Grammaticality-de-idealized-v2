// revised-engine.mjs -- v2 quantitative core for the current OVMG manuscript.
//
// This module is deliberately separate from engine.js. The browser lab and its
// fixtures implement the 2026-07-09 prototype; this is the reference core for
// the revised Sections 3--4. It implements three commitments:
//
//   1. Discount evidence, not the baseline prior.
//   2. Treat weighted streams as generalized-Bayes effective evidence.
//   3. Derive omission evidence from normalized gated-choice likelihoods.
//
// It is an executable model contract, not a fitted empirical model. In
// particular, its independent speaker inclusion draws are a default that a
// latent-lect model can replace when assembly-level co-licensing is material.

function requireFinite(value, name) {
  if (!Number.isFinite(value)) {
    throw new TypeError(`${name} must be finite, got ${value}`);
  }
}

function requireNonnegative(value, name) {
  requireFinite(value, name);
  if (value < 0) throw new RangeError(`${name} must be non-negative, got ${value}`);
}

function requireProbability(value, name) {
  requireFinite(value, name);
  if (value < 0 || value > 1) {
    throw new RangeError(`${name} must be in [0, 1], got ${value}`);
  }
}

/**
 * Evidence state for one construction--situation pair. The prior and the
 * discounted effective counts are intentionally stored separately, so a quiet
 * node returns to its stated prior rather than to an improper Beta(0, 0).
 */
export function makeEvidenceState({
  priorA = 1,
  priorB = 1,
  positiveEvidence = 0,
  negativeEvidence = 0,
} = {}) {
  if (!(priorA > 0) || !(priorB > 0)) {
    throw new RangeError(`Beta prior parameters must be positive, got ${priorA}, ${priorB}`);
  }
  requireNonnegative(positiveEvidence, 'positiveEvidence');
  requireNonnegative(negativeEvidence, 'negativeEvidence');
  return { priorA, priorB, positiveEvidence, negativeEvidence };
}

/** Posterior parameters constructed from fixed prior plus effective evidence. */
export function posteriorParameters(state) {
  return {
    a: state.priorA + state.positiveEvidence,
    b: state.priorB + state.negativeEvidence,
  };
}

/**
 * Baseline-preserving discounted update. `positive` and `negative` are
 * effective counts, not literal Bernoulli observations. Their scale must be
 * calibrated against repeated-sampling variance before empirical fitting.
 */
export function updateEvidence(state, evidence = {}, params = {}) {
  const { positive = 0, negative = 0 } = evidence;
  const { deltaM = 1, lambdaPos = 1, lambdaNeg = 1 } = params;
  if (!(deltaM > 0) || deltaM > 1) {
    throw new RangeError(`deltaM must be in (0, 1], got ${deltaM}`);
  }
  requireNonnegative(positive, 'positive');
  requireNonnegative(negative, 'negative');
  requireNonnegative(lambdaPos, 'lambdaPos');
  requireNonnegative(lambdaNeg, 'lambdaNeg');
  return {
    priorA: state.priorA,
    priorB: state.priorB,
    positiveEvidence: deltaM * state.positiveEvidence + lambdaPos * positive,
    negativeEvidence: deltaM * state.negativeEvidence + lambdaNeg * negative,
  };
}

/** Posterior mean C_t for a single pivotal node. */
export function mean(state) {
  const { a, b } = posteriorParameters(state);
  return a / (a + b);
}

/** Posterior concentration nu_t for a single pivotal node. */
export function concentration(state) {
  const { a, b } = posteriorParameters(state);
  return a + b;
}

/** Var(theta | D): epistemic uncertainty about the population licensing rate. */
export function epistemicVariance(state) {
  const m = mean(state);
  return (m * (1 - m)) / (concentration(state) + 1);
}

/** E[theta(1-theta) | D]: predictive between-speaker heterogeneity. */
export function heterogeneityVariance(state) {
  const m = mean(state);
  const nu = concentration(state);
  return (m * (1 - m) * nu) / (nu + 1);
}

/** Convenience summary for logging and test assertions. */
export function summary(state) {
  const { a, b } = posteriorParameters(state);
  return {
    a,
    b,
    mean: mean(state),
    concentration: concentration(state),
    epistemicVariance: epistemicVariance(state),
    heterogeneityVariance: heterogeneityVariance(state),
  };
}

// Numerics for the decision-confidence read-out. This is a local copy rather
// than an import from the frozen v1 engine: v2 must remain self-contained.
const LANCZOS_G = 7;
const LANCZOS_C = [
  0.99999999999980993, 676.5203681218851, -1259.1392167224028,
  771.32342877765313, -176.61502916214059, 12.507343278686905,
  -0.13857109526572012, 9.9843695780195716e-6, 1.5056327351493116e-7,
];

function logGamma(value) {
  if (value < 0.5) {
    return Math.log(Math.PI / Math.sin(Math.PI * value)) - logGamma(1 - value);
  }
  const shifted = value - 1;
  let sum = LANCZOS_C[0];
  for (let index = 1; index < LANCZOS_C.length; index += 1) {
    sum += LANCZOS_C[index] / (shifted + index);
  }
  const t = shifted + LANCZOS_G + 0.5;
  return 0.5 * Math.log(2 * Math.PI) + (shifted + 0.5) * Math.log(t) - t + Math.log(sum);
}

function betaContinuedFraction(x, a, b) {
  const maxIterations = 300;
  const epsilon = 3e-15;
  const floor = 1e-300;
  const sum = a + b;
  const aPlusOne = a + 1;
  const aMinusOne = a - 1;
  let c = 1;
  let d = 1 - (sum * x) / aPlusOne;
  if (Math.abs(d) < floor) d = floor;
  d = 1 / d;
  let result = d;
  for (let step = 1; step <= maxIterations; step += 1) {
    const twice = 2 * step;
    let coefficient = (step * (b - step) * x) / ((aMinusOne + twice) * (a + twice));
    d = 1 + coefficient * d;
    if (Math.abs(d) < floor) d = floor;
    c = 1 + coefficient / c;
    if (Math.abs(c) < floor) c = floor;
    d = 1 / d;
    result *= d * c;
    coefficient = (-(a + step) * (sum + step) * x) /
      ((a + twice) * (aPlusOne + twice));
    d = 1 + coefficient * d;
    if (Math.abs(d) < floor) d = floor;
    c = 1 + coefficient / c;
    if (Math.abs(c) < floor) c = floor;
    d = 1 / d;
    const change = d * c;
    result *= change;
    if (Math.abs(change - 1) < epsilon) return result;
  }
  throw new Error('beta continued fraction failed to converge');
}

/** Regularized incomplete Beta CDF at x for Beta(a, b). */
export function betaCdf(x, a, b) {
  requireProbability(x, 'x');
  if (!(a > 0) || !(b > 0)) {
    throw new RangeError(`Beta parameters must be positive, got ${a}, ${b}`);
  }
  if (x === 0) return 0;
  if (x === 1) return 1;
  const logFront = logGamma(a + b) - logGamma(a) - logGamma(b) +
    a * Math.log(x) + b * Math.log(1 - x);
  const front = Math.exp(logFront);
  if (x < (a + 1) / (a + b + 2)) {
    return (front * betaContinuedFraction(x, a, b)) / a;
  }
  return 1 - (front * betaContinuedFraction(1 - x, b, a)) / b;
}

/** Posterior probability that a node's population rate meets a decision threshold. */
export function posteriorProbabilityAtLeast(state, threshold) {
  requireProbability(threshold, 'threshold');
  if (threshold === 0) return 1;
  if (threshold === 1) return 0;
  const { a, b } = posteriorParameters(state);
  return 1 - betaCdf(threshold, a, b);
}

/**
 * Decision confidence Phi_dec: certainty about which side of the membership
 * threshold the population rate lies. It can remain low for a precisely known
 * interior population rate, unlike concentration-based evidence confidence.
 */
export function decisionConfidence(state, threshold = 0.5) {
  const probabilityAtLeast = posteriorProbabilityAtLeast(state, threshold);
  return Math.max(probabilityAtLeast, 1 - probabilityAtLeast);
}

/**
 * Normalized gated softmax for a speaker's available candidate set. The
 * outside option is always available. `availability[k]` is that speaker's
 * inclusion state for candidate k in the relevant situation.
 */
export function gatedChoiceProbabilities({ utilities, availability, outsideUtility = 0 }) {
  if (!Array.isArray(utilities) || !Array.isArray(availability)) {
    throw new TypeError('utilities and availability must be arrays');
  }
  if (utilities.length !== availability.length || utilities.length === 0) {
    throw new RangeError('utilities and availability must have the same non-zero length');
  }
  utilities.forEach((utility, index) => requireFinite(utility, `utilities[${index}]`));
  availability.forEach((available, index) => {
    if (typeof available !== 'boolean') {
      throw new TypeError(`availability[${index}] must be boolean`);
    }
  });
  requireFinite(outsideUtility, 'outsideUtility');

  const activeUtilities = [outsideUtility];
  for (let index = 0; index < utilities.length; index += 1) {
    if (availability[index]) activeUtilities.push(utilities[index]);
  }
  const maxUtility = Math.max(...activeUtilities);
  const outsideWeight = Math.exp(outsideUtility - maxUtility);
  const weights = utilities.map((utility, index) => (
    availability[index] ? Math.exp(utility - maxUtility) : 0
  ));
  const normalizer = outsideWeight + weights.reduce((total, weight) => total + weight, 0);
  return {
    candidates: weights.map((weight) => weight / normalizer),
    outside: outsideWeight / normalizer,
  };
}

/** Probability of an observable candidate index or the outside option. */
export function outcomeProbability(probabilities, outcome) {
  if (outcome === 'outside') return probabilities.outside;
  if (!Number.isInteger(outcome) || outcome < 0 || outcome >= probabilities.candidates.length) {
    throw new RangeError(`outcome must be a candidate index or 'outside', got ${outcome}`);
  }
  return probabilities.candidates[outcome];
}

/**
 * Log evidence against target availability from a non-target outcome:
 * log P(y | target unavailable) - log P(y | target available).
 */
export function omissionLogLikelihoodRatio({
  probabilityIfAvailable,
  probabilityIfUnavailable,
}) {
  requireProbability(probabilityIfAvailable, 'probabilityIfAvailable');
  requireProbability(probabilityIfUnavailable, 'probabilityIfUnavailable');
  if (probabilityIfAvailable === 0 || probabilityIfUnavailable === 0) {
    throw new RangeError('omission likelihoods must be positive for a finite log ratio');
  }
  return Math.log(probabilityIfUnavailable) - Math.log(probabilityIfAvailable);
}

/** Split a recoverability-weighted log likelihood ratio into evidence streams. */
export function routeOmissionEvidence({ logLikelihoodRatio, recoverability = 1 }) {
  requireFinite(logLikelihoodRatio, 'logLikelihoodRatio');
  requireProbability(recoverability, 'recoverability');
  return {
    positive: recoverability * Math.max(-logLikelihoodRatio, 0),
    negative: recoverability * Math.max(logLikelihoodRatio, 0),
  };
}

/**
 * Exact counterfactual omission evidence under the gated-choice model. A
 * target token itself is direct positive evidence and must not be routed here.
 */
export function omissionEvidenceFromChoice({
  utilities,
  availability,
  targetIndex,
  observedOutcome,
  outsideUtility = 0,
  recoverability = 1,
}) {
  if (!Number.isInteger(targetIndex) || targetIndex < 0 || targetIndex >= utilities.length) {
    throw new RangeError(`targetIndex must identify a candidate, got ${targetIndex}`);
  }
  if (observedOutcome === targetIndex) {
    throw new RangeError('target production is direct positive evidence, not an omission');
  }
  const available = availability.slice();
  const unavailable = availability.slice();
  available[targetIndex] = true;
  unavailable[targetIndex] = false;
  const pAvailable = outcomeProbability(
    gatedChoiceProbabilities({ utilities, availability: available, outsideUtility }),
    observedOutcome,
  );
  const pUnavailable = outcomeProbability(
    gatedChoiceProbabilities({ utilities, availability: unavailable, outsideUtility }),
    observedOutcome,
  );
  const logLikelihoodRatio = omissionLogLikelihoodRatio({
    probabilityIfAvailable: pAvailable,
    probabilityIfUnavailable: pUnavailable,
  });
  return {
    probabilityIfAvailable: pAvailable,
    probabilityIfUnavailable: pUnavailable,
    logLikelihoodRatio,
    ...routeOmissionEvidence({ logLikelihoodRatio, recoverability }),
  };
}

/** A bounded simulation link for the Section 4 repair channel. */
export function repairProbability({
  baseline = 0,
  statusEstimate = 1,
  divergence = 0,
  footing = 1,
  gain = 1,
}) {
  requireProbability(baseline, 'baseline');
  requireProbability(statusEstimate, 'statusEstimate');
  requireNonnegative(divergence, 'divergence');
  requireNonnegative(footing, 'footing');
  requireProbability(gain, 'gain');
  const divergenceResponse = 1 - Math.exp(-divergence * footing);
  return baseline + (1 - baseline) * gain * (1 - statusEstimate) * divergenceResponse;
}

/** Expected repair flow, N * P(mis-set) * r(Delta, footing). */
export function repairFlow({ opportunities, misSetProbability, repairResponse }) {
  requireNonnegative(opportunities, 'opportunities');
  requireProbability(misSetProbability, 'misSetProbability');
  requireProbability(repairResponse, 'repairResponse');
  return opportunities * misSetProbability * repairResponse;
}
