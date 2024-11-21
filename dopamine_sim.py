import numpy as np

# Activities and their reward probabilities
stimuli_reward = {
    "exercise": 0.2,
    "gaming": 0.57,
    "reading": 0.08,
}

# Number of iterations and stimuli
runs = 50000
n_stimuli = len(stimuli_reward)

def decay(V, selected_stimulus, decay_rate=0.05, min_value=0.1):
    V[selected_stimulus] = max(V[selected_stimulus] * (1 - decay_rate), min_value)
    return V

# Extract keys from dictionary
stimuli_keys = list(stimuli_reward.keys())

# Initialise dataset X (indicating actual rewards for each stimulus)
X = np.zeros((runs, n_stimuli))
for element in range(runs):
    for prob in range(n_stimuli):
        if np.random.rand() < stimuli_reward[stimuli_keys[prob]]:
            X[element][prob] = 1

# Initialize reward counters
"""
Alpha - Positive rewards
Beta - Negative rewards
V - Expected reward (Rescorla-Wagner value)
""" 
alpha = np.zeros(n_stimuli)
beta = np.zeros(n_stimuli)
V = np.array([0.2, 0.7, 0.1])  # Initialise expected rewards (V) for each stimulus

# Learning rate for the Rescorla Wagner model
learning_rate = 0.3

# Thompson sampling to determine best stimuli per iteration
for element in range(runs):
    selected_stimulus = 0
    max_random = 0
    for stimulus in range(n_stimuli):
        # Use beta distribution to collect sample for each stimulus
        random_beta = np.random.beta(alpha[stimulus] + 1, beta[stimulus] + 1)
        weighted_sample = random_beta * V[stimulus] # Takes into accordance expected reward (V)
        if weighted_sample > max_random:
            max_random = weighted_sample 
            selected_stimulus = stimulus

    # Get the actual reward for the selected stimulus
    actual_reward = X[element][selected_stimulus]
    
    # Calculate Prediction Error using Rescorla Wagner model
    prediction_error = actual_reward - V[selected_stimulus]
    
    # Update Expected Reward (V) using Rescorla Wagner equation
    V[selected_stimulus] += learning_rate * prediction_error

    # Update alpha and beta based on the outcome (Bayesian update)
    """
    WHERE:
    Alpha - Positive reward
    Beta - Negative reward
    """
    if actual_reward == 1:
        alpha[selected_stimulus] += 0.1
        V = decay(V, selected_stimulus, decay_rate=0.05, min_value=0.1)
    else:
        beta[selected_stimulus] += 0.1

# Output positive feedback per stimulus
for stimuli_index, stimuli_name in enumerate(stimuli_keys):
    print(f"{stimuli_name}: {int(alpha[stimuli_index])} positive feedbacks")

# Derive which action received highest reward
best_stimulus_index = np.argmax(alpha)
best_stimulus_name = stimuli_keys[best_stimulus_index]

print(f"The action which stimulated dopamine receptors the most is: {best_stimulus_name}")

print(f"{best_stimulus_index}")