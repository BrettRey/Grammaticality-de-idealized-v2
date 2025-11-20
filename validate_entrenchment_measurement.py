import numpy as np
import pandas as pd
from sklearn.decomposition import FactorAnalysis
from scipy import stats
import matplotlib.pyplot as plt

# 1. Generate true C^t values for 1000 constructions
np.random.seed(42)
n_items = 1000
true_C = np.random.beta(2, 5, n_items)  # Beta dist gives realistic 0-1 values

# 2. Set factor loadings (these would be estimated in real data)
lambda_A = 1.0      # Fixed for identification
lambda_E = 0.8      # Log exposure frequency 
lambda_P = 0.9      # Production probability
lambda_S = 0.7      # Social acceptability

# 3. Generate observable indicators with measurement error
sigma_A = 0.15
sigma_E = 0.25  
sigma_P = 0.20
sigma_S = 0.30

A = lambda_A * true_C + np.random.normal(0, sigma_A, n_items)
A = np.clip(A, 0, 1)  # Keep in [0,1]

log_E = lambda_E * true_C + np.random.normal(0, sigma_E, n_items)
E = np.exp(log_E)  # Convert back to counts

P = lambda_P * true_C + np.random.normal(0, sigma_P, n_items)
P = np.clip(P, 0, 1)

S = lambda_S * true_C + np.random.normal(0, sigma_S, n_items)
S = np.clip(S, 0, 1)

# 4. Recover C^t using factor analysis
indicators = np.column_stack([A, np.log(E), P, S])
fa = FactorAnalysis(n_components=1)
recovered_C = fa.fit_transform(indicators).flatten()

# Rescale to [0,1] for comparison
recovered_C = (recovered_C - recovered_C.min()) / (recovered_C.max() - recovered_C.min())

# 5. Evaluate recovery
rmse = np.sqrt(np.mean((true_C - recovered_C)**2))
correlation = np.corrcoef(true_C, recovered_C)[0,1]

print(f"RMSE: {rmse:.3f}")
print(f"Correlation: {correlation:.3f}")
