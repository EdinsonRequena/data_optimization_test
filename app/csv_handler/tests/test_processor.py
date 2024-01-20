import pandas as pd
from pandas.testing import assert_frame_equal

import pytest
from app.csv_handler.processor import read_csv


@pytest.fixture(scope="module")
def test_csv_file(tmpdir_factory):
    """
    Fixture that creates a temporary CSV file with test data.

    Args:
        tmpdir_factory: A pytest fixture that provides a temporary directory.

    Returns:
        str: The path of the created CSV file.
    """
    csv_data = """PointOfSale;Product;Date;Stock
Store1;ProductA;2024-01-01;100
Store2;ProductB;2024-01-02;150"""
    file = tmpdir_factory.mktemp("data").join("Stock_test.csv")
    file.write(csv_data)

    return str(file)


def test_read_csv(test_csv_file):  # pylint: disable=redefined-outer-name
    """
    Test case for the read_csv function.

    Parameters:
    - test_csv_file: str
        The path to the test CSV file.
    """

    df = read_csv(test_csv_file)

    # Crear un DataFrame esperado
    expected_data = {
        'PointOfSale': ['Store1', 'Store2'],
        'Product': ['ProductA', 'ProductB'],
        'Date': [pd.Timestamp('2024-01-01'), pd.Timestamp('2024-01-02')],
        'Stock': [100, 150]
    }
    expected_df = pd.DataFrame(expected_data)

    # Verificar que el DataFrame leído sea igual al esperado
    assert_frame_equal(df, expected_df)
