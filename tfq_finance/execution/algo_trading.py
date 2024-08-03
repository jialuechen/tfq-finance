import numpy as np
import pandas as pd

def vwap_execution(volume, target_percentage):
    executed_volume = volume * target_percentage
    return executed_volume

def twap_execution(volume, num_intervals):
    executed_volume = volume / num_intervals
    return np.full(num_intervals, executed_volume)

if __name__ == "__main__":
    volume = 10000
    target_percentage = 0.1
    num_intervals = 10

    vwap = vwap_execution(volume, target_percentage)
    twap = twap_execution(volume, num_intervals)

    print(f"VWAP Execution Volume: {vwap}")
    print(f"TWAP Execution Volumes: {twap}")