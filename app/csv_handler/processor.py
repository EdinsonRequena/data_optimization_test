import pandas as pd


def read_csv(file_path):
    """
    Read a CSV file and return a pandas DataFrame.

    Parameters:
    file_path (str): The path to the CSV file.

    Returns:
    pandas.DataFrame: The DataFrame containing the CSV data.
    """
    dtype = {
        'PointOfSale': str,
        'Product': str,
        'Stock': int
    }

    parse_dates = ['Date']
    use_columns = ['PointOfSale', 'Product', 'Date', 'Stock']
    return pd.read_csv(
        file_path,
        delimiter=';',
        dtype=dtype,
        parse_dates=parse_dates,
        usecols=use_columns,
        low_memory=False,
    )
