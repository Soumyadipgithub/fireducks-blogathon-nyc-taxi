import fireducks as fd  
import pandas as pd  
from utils import evaluate  # NEW: Import evaluation trigger

def load_data(filepath):  
    if filepath.endswith('.parquet'):
        df = fd.read_parquet(filepath, parallel=True)
    else:
        df = fd.read_csv(filepath, parallel=True)
    
    evaluate(df)  # NEW: Force computation after loading
    return df  

def clean_data(df):  
    # Filter invalid fares (FireDucks handles in-place)
    df = df[df['fare_amount'] > 0]  
    
    # Fill missing values
    df['passenger_count'] = df['passenger_count'].fillna(1)
    
    evaluate(df)  # NEW: Ensure cleaning ops execute
    return df  

def analyze_data(df):  
    # Perform aggregation
    result = df.groupby('PULocationID').agg({'fare_amount': 'mean'})
    
    evaluate(result)  # NEW: Trigger computation before conversion
    return result.to_pandas()  # Convert to Pandas for compatibility

if __name__ == "__main__":  
    df = load_data("data/nyc_taxi_2020.parquet")  
    cleaned_df = clean_data(df)  
    analysis = analyze_data(cleaned_df)  
    print(analysis.head())
