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

print("=== FIREDUCKS DATA LOADING ===")
print(f"File: {file_path}")
print("Loading with FireDucks...")

start_time = time.time()
import fireducks as fd
df_fireducks = fd.read_csv(file_path, parallel=True)
fireducks_time = time.time() - start_time

print(f"\nData loaded successfully!")
print(f"Time taken: {fireducks_time:.2f} seconds")
print("=== LOADING COMPLETE ===")

# Keep the terminal open
input("\nPress Enter to exit...") 