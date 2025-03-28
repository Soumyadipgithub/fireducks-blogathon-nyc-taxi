import time
import os
import sys

# Get the project root directory
script_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(script_dir) if "code" in script_dir else script_dir

# Path to data file
file_path = os.path.join(project_root, "data", "nyc_taxi_2020.csv")

print("=== PANDAS DATA LOADING ===")
print(f"File: {file_path}")
print("Loading with Pandas...")

start_time = time.time()
import pandas as pd
df_pandas = pd.read_csv(file_path)
pandas_time = time.time() - start_time

print(f"\nRows loaded: {len(df_pandas)}")
print(f"Time taken: {pandas_time:.2f} seconds")
print("=== LOADING COMPLETE ===")

# Keep the terminal open
input("\nPress Enter to exit...") 