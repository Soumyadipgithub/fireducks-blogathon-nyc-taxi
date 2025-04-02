def evaluate(df):  
    """Force computation for FireDucks' lazy evaluation"""  
    try:  
        # FireDucks-specific evaluation  
        df._evaluate()  
    except AttributeError:  
        # No action needed for Pandas/other tools  
        pass  
