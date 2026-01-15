import pandas as pd

def load(path: str) -> pd.DataFrame | None: 
    """
    Load a CSV file into a pandas DataFrame.
    """

    try:
        assert path and isinstance(path, str), "Path must be a non-empty string."
        assert path.endswith('.csv'), "Unsupported file format. Use .csv files."
        file = pd.read_csv(path)
        assert not file.empty, "The CSV file is empty."
    except FileNotFoundError:
        print(f"CSV file not found at path: {path}")
        return None
    except AssertionError as e:
        print(f'AssertionError: {e}')
        return None
    except Exception as e:
        print(f"An error occurred while loading the CSV file: {e}")
        return None
    print(f'Loading dataset of dimensions {file.shape}')
    return file
