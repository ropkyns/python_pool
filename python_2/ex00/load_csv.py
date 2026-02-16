import pandas as pd


def load(path: str) -> pd.DataFrame:
    try:
        assert path != "", "Path null"
        assert path.endswith(".csv"), "File is not a .csv"
        df = pd.read_csv(path)
        assert df is not None, "File not found"
        print(f"Loading dataset of dimensions {df.shape}")
        return (df)
    except Exception as error:
        print(f"Error: {error}")
        return None
