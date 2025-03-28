import time  
import pandas as pd  
import fireducks as fd  

def benchmark_load(filepath):  
    # Pandas  
    start = time.time()  
    if filepath.endswith('.parquet'):
        df_pandas = pd.read_parquet(filepath)
    else:
        df_pandas = pd.read_csv(filepath)  
    pandas_time = time.time() - start  

    # FireDucks  
    start = time.time()  
    if filepath.endswith('.parquet'):
        df_fireducks = fd.read_parquet(filepath, parallel=True)
    else:
        df_fireducks = fd.read_csv(filepath, parallel=True)  
    fireducks_time = time.time() - start  

    return pandas_time, fireducks_time  

if __name__ == "__main__":  
    pandas_time, fireducks_time = benchmark_load("data/nyc_taxi_2020.parquet")  
    print(f"Pandas: {pandas_time:.2f}s | FireDucks: {fireducks_time:.2f}s")  