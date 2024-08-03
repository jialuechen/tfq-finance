import numpy as np

def calculate_cyber_risk(exposure, cyber_event_probability, loss_given_cyber_event):
    expected_loss = exposure * cyber_event_probability * loss_given_cyber_event
    return expected_loss

if __name__ == "__main__":
    exposure = 1000000
    cyber_event_probability = 0.02
    loss_given_cyber_event = 0.5

    expected_loss = calculate_cyber_risk(exposure, cyber_event_probability, loss_given_cyber_event)
    print(f"Expected Cyber Loss: {expected_loss}")