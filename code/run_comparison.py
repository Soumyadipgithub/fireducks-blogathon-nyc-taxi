import time
import os
import sys

# Add the current directory to Python path so fireducks module can be imported
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Get the project root directory
script_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(script_dir) if "code" in script_dir else script_dir

# Path to data file
file_path = os.path.join(project_root, "data", "nyc_taxi_2020.csv")

print("==== COMPARISON: PANDAS VS FIREDUCKS ====")
print(f"File: {file_path}")
print("----------------------------------------")

# Pandas timing
print("Loading with Pandas...")
start_time = time.time()
import pandas as pd
df_pandas = pd.read_csv(file_path)
pandas_time = time.time() - start_time
print(f"Pandas loaded {len(df_pandas)} rows in {pandas_time:.2f} seconds")
print("----------------------------------------")

# FireDucks timing
print("Loading with FireDucks...")
start_time = time.time()
import fireducks as fd
df_fireducks = fd.read_csv(file_path, parallel=True)
fireducks_time = time.time() - start_time
print(f"FireDucks loaded data in {fireducks_time:.2f} seconds")
print("----------------------------------------")

# Calculate speedup
speedup = pandas_time / fireducks_time
print(f"Result: FireDucks is {speedup:.2f}x faster than Pandas!")
print("==== COMPARISON COMPLETE ====") 