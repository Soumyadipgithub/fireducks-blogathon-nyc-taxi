def evaluate(df):
    """Force computation for FireDucks' lazy evaluation"""
    try:
        df._evaluate()  # FireDucks-specific method
    except AttributeError:
        try:
            df.collect()  # For Polars compatibility
        except AttributeError:
            pass  # No action for Pandas
