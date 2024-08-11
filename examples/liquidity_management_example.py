import numpy as np
from tfq_finance.optimization.liquidity_management import manage_liquidity

def liquidity_management_example():
    cash_flows = np.random.randn(100)
    liquidity_needs = 0.05

    liquidity_plan = manage_liquidity(cash_flows, liquidity_needs)
    print("Liquidity Management Plan:", liquidity_plan)

if __name__ == "__main__":
    liquidity_management_example()