import numpy as np

def calculate_catastrophe_risk(exposure, event_probability, loss_given_event, num_simulations=10000):
    simulated_losses = np.random.binomial(1, event_probability, num_simulations) * exposure * loss_given_event
    expected_loss = np.mean(simulated_losses)
    var_99 = np.percentile(simulated_losses, 99)
    return expected_loss, var_99

if __name__ == "__main__":
    exposure = 1000000
    event_probability = 0.01
    loss_given_event = 0.8

    expected_loss, var_99 = calculate_catastrophe_risk(exposure, event_probability, loss_given_event)
    print(f"Expected Catastrophe Loss: {expected_loss}")
    print(f"99th Percentile VaR: {var_99}")