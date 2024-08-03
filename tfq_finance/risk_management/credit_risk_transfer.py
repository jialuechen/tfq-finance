import numpy as np

def transfer_credit_risk(exposure, transfer_amount, protection_rate):
    remaining_exposure = exposure - transfer_amount
    cost_of_protection = transfer_amount * protection_rate
    return remaining_exposure, cost_of_protection

if __name__ == "__main__":
    exposure = 1000000
    transfer_amount = 500000
    protection_rate = 0.02

    remaining_exposure, cost_of_protection = transfer_credit_risk(exposure, transfer_amount, protection_rate)
    print(f"Remaining Exposure: {remaining_exposure}")
    print(f"Cost of Protection: {cost_of_protection}")