from joblib import Parallel, delayed
import numpy as np

def parallel_process(function, data, n_jobs=-1):
    results = Parallel(n_jobs=n_jobs)(delayed(function)(d) for d in data)
    return results

if __name__ == "__main__":
    def example_function(x):
        return x ** 2

    data = np.arange(10)
    results = parallel_process(example_function, data)
    print("Parallel Processing Results:")
    print(results)