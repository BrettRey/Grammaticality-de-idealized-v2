
import numpy as np

# Simulation parameters
steps = 50
np.random.seed(42)

def simulate_trajectory(n_opportunities_per_step, rho, s_rate=0.0):
    # Initial Beta prior
    a = 1.0
    b = 1.0
    
    means = []
    lower = []
    upper = []
    
    current_a = a
    current_b = b
    
    for t in range(steps):
        # Calculate mean
        mean_c = current_a / (current_a + current_b)
        means.append(mean_c)
        
        # Calculate credible interval (optional, using variance proxy or just skipping)
        # For simple plotting, we'll just plot mean
        
        # Simulate evidence
        # Preemption mass p_t
        p_t = n_opportunities_per_step * rho
        
        # Positive evidence s_t (assuming we never see it for 'ungrammatical/missing' forms)
        # For the 'rare licensed' case, maybe we see it rarely? 
        # But the point is to distinguish 'unseen rare' from 'unseen blocked'.
        # Let's assume s_t = 0 for both to show the inference difference.
        s_t = 0 
        
        # Error evidence e_t
        e_t = 0.0
        
        # Update
        current_a += s_t
        current_b += e_t + p_t
        
    return means

# Scenario 1: Rare / Community-Novel (e.g. friend of whose)
# Low opportunity count, so p_t accumulation is slow
traj_rare = simulate_trajectory(n_opportunities_per_step=0.2, rho=0.5)

# Scenario 2: Stable Gap (e.g. LBE)
# High opportunity count (common niche), high rho (would be useful), so p_t accumulation is fast
traj_gap = simulate_trajectory(n_opportunities_per_step=10.0, rho=0.5)

# Output for PGFPlots
print("step rare gap")
for i in range(steps):
    print(f"{i} {traj_rare[i]:.4f} {traj_gap[i]:.4f}")
