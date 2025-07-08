import pandas as pd
def load_bike_data(filepath):
    try:
        df = pd.read_csv(filepath)
        print(f"Loaded {df.shape[0]} rows and {df.shape[1]} columns.")
        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        return None
