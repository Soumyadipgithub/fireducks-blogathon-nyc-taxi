import fireducks as fd  
import pandas as pd  

# Load data with FireDucks  
def load_data(filepath):  
    if filepath.endswith('.parquet'):
        df = fd.read_parquet(filepath, parallel=True)
    else:
        df = fd.read_csv(filepath, parallel=True)  
    return df  

# Clean and filter data  
def clean_data(df):  
    df = df[df['fare_amount'] > 0]  
    df['passenger_count'] = df['passenger_count'].fillna(1)  
    return df  

# Aggregation example  
def analyze_data(df):  
    result = df.groupby('PULocationID').agg({'fare_amount': 'mean'})  
    return result.to_pandas()  

if __name__ == "__main__":  
    df = load_data("data/nyc_taxi_2020.parquet")  
    cleaned_df = clean_data(df)  
    analysis = analyze_data(cleaned_df)  
    print(analysis.head())  