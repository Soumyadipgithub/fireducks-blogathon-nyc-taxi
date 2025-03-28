import pandas as pd
import multiprocessing as mp
from functools import partial

class FireDucksDataFrame:
    def __init__(self, pandas_df):
        self.df = pandas_df
    
    def __getitem__(self, key):
        if isinstance(key, FireDucksDataFrame):
            # This handles boolean indexing with a FireDucksDataFrame mask
            return FireDucksDataFrame(self.df[key.df])
        return FireDucksDataFrame(self.df[key])
    
    def __setitem__(self, key, value):
        if isinstance(value, FireDucksDataFrame):
            self.df[key] = value.df
        else:
            self.df[key] = value
    
    def fillna(self, value):
        return FireDucksDataFrame(self.df.fillna(value))
    
    def groupby(self, by):
        return FireDucksGroupBy(self.df.groupby(by))
    
    def to_pandas(self):
        return self.df
        
    def __gt__(self, other):
        return FireDucksDataFrame(self.df > other)
        
    def __lt__(self, other):
        return FireDucksDataFrame(self.df < other)
        
    def __ge__(self, other):
        return FireDucksDataFrame(self.df >= other)
        
    def __le__(self, other):
        return FireDucksDataFrame(self.df <= other)
        
    def __eq__(self, other):
        return FireDucksDataFrame(self.df == other)
        
    def __ne__(self, other):
        return FireDucksDataFrame(self.df != other)

class FireDucksGroupBy:
    def __init__(self, pandas_groupby):
        self.groupby = pandas_groupby
    
    def agg(self, agg_dict):
        return FireDucksDataFrame(self.groupby.agg(agg_dict))

def _read_chunk(args):
    chunk_path, kwargs = args
    return pd.read_csv(chunk_path, **kwargs)

def read_csv(filepath, parallel=False, **kwargs):
    """
    Read a CSV file into a FireDucksDataFrame, with optional parallelism
    """
    if parallel:
        # For demonstration, we're not actually reading in parallel
        # Just using pandas but wrapping in our class
        df = pd.read_csv(filepath, **kwargs)
    else:
        df = pd.read_csv(filepath, **kwargs)
    
    return FireDucksDataFrame(df)

def read_parquet(filepath, parallel=False, **kwargs):
    """
    Read a Parquet file into a FireDucksDataFrame, with optional parallelism
    """
    if parallel:
        # For demonstration, we're not actually reading in parallel
        # Just using pandas but wrapping in our class
        df = pd.read_parquet(filepath, **kwargs)
    else:
        df = pd.read_parquet(filepath, **kwargs)
    
    return FireDucksDataFrame(df) 