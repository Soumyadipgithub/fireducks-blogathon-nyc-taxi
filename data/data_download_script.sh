#!/bin/bash  

# Download NYC Taxi Data (2020, 10K rows sample)  
wget -O data/nyc_taxi_2020.csv "https://github.com/yourusername/fireducks-blogathon-nyc-taxi/raw/main/data/nyc_taxi_2020.csv"  

# For full dataset (comment the above and uncomment below):  
# wget -O data/nyc_taxi_2020.csv "https://s3.amazonaws.com/nyc-tlc/trip+data/yellow_tripdata_2020-01.csv"  