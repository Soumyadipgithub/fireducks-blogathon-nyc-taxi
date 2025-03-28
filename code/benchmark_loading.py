import time
import pandas as pd
import fireducks as fd
import os

def benchmark_data_loading(file_path):
    # Check if it's a Parquet file
    is_parquet = file_path.endswith('.parquet')
    
    try:
        # Benchmark Pandas
        start_pandas = time.time()
        if is_parquet:
            df_pandas = pd.read_parquet(file_path)
        else:
            df_pandas = pd.read_csv(file_path)
        pandas_time = time.time() - start_pandas
        print(f"Pandas loaded data in {pandas_time:.2f} seconds")
    except Exception as e:
        print(f"Error loading with Pandas: {e}")
        pandas_time = None

    try:
        # Benchmark FireDucks
        start_fireducks = time.time()
        if is_parquet:
            df_fireducks = fd.read_parquet(file_path, parallel=True)
        else:
            df_fireducks = fd.read_csv(file_path, parallel=True)
        fireducks_time = time.time() - start_fireducks
        print(f"FireDucks loaded data in {fireducks_time:.2f} seconds")
    except Exception as e:
        print(f"Error loading with FireDucks: {e}")
        fireducks_time = None

    return pandas_time, fireducks_time

if __name__ == "__main__":
    # Get the project root directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir) if "code" in script_dir else script_dir
    
    # Path to data file
    file_path = os.path.join(project_root, "data", "nyc_taxi_2020.csv")
    
    print(f"Using data file: {file_path}")
    pandas_time, fireducks_time = benchmark_data_loading(file_path)
    
    if pandas_time and fireducks_time:
        speedup = pandas_time / fireducks_time
        print(f"FireDucks is {speedup:.2f}x faster than Pandas")