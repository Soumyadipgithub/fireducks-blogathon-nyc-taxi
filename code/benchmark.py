import time
import pandas as pd
import fireducks as fd
from utils import evaluate  # NEW: Required for FireDucks evaluation

def benchmark_load(filepath):
    """Benchmark data loading with 3 warm-aware iterations"""
    # Warm-up FireDucks (first run not measured)
    if filepath.endswith('.parquet'):
        fd.read_parquet(filepath, parallel=True)._evaluate()
    else:
        fd.read_csv(filepath, parallel=True)._evaluate()

    pandas_times = []
    fireducks_times = []

    for _ in range(3):  # NEW: 3 iterations for median calculation
        # Benchmark Pandas
        start = time.time()
        if filepath.endswith('.parquet'):
            pd.read_parquet(filepath)
        else:
            pd.read_csv(filepath)
        pandas_times.append(time.time() - start)

        # Benchmark FireDucks
        start = time.time()
        if filepath.endswith('.parquet'):
            df = fd.read_parquet(filepath, parallel=True)
        else:
            df = fd.read_csv(filepath, parallel=True)
        evaluate(df)  # NEW: Force computation
        fireducks_times.append(time.time() - start)

    # Return median values
    return (
        sorted(pandas_times)[1],    # Pandas median
        sorted(fireducks_times)[1]  # FireDucks median
    )

if __name__ == "__main__":
    pandas_median, fireducks_median = benchmark_load("data/nyc_taxi_2020.parquet")
    print(f"Pandas Median: {pandas_median:.2f}s | FireDucks Median: {fireducks_median:.2f}s")
