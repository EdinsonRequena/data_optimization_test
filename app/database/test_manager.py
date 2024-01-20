from datetime import datetime

import pytest
from app.database.manager import DatabaseManager


@pytest.fixture(scope="module")
def db_manager():
    """
    Fixture that creates a DatabaseManager instance.

    Returns:
        DatabaseManager: The DatabaseManager instance.
    """

    with DatabaseManager() as manager:
        yield manager


def test_create_table(db_manager):  # pylint: disable=redefined-outer-name
    """
    Test case for the create_table method of the DatabaseManager class.
    """

    db_manager.clean_table("inventory")
    db_manager.create_table()

    with db_manager.conn.cursor() as cursor:
        cursor.execute(
            "SELECT EXISTS (SELECT FROM information_schema.tables WHERE table_name = %s);",
            ("inventory",)
        )
        query_result = cursor.fetchone()[0]
        assert query_result is True


def test_clean_table(db_manager):  # pylint: disable=redefined-outer-name
    """
    Test case for the clean_table method of the DatabaseManager class.
    """

    db_manager.create_table()
    db_manager.create_table()
    inventory_row = [("Store1", "ProductA", "2024-01-01", 100)]
    db_manager.insert_data(inventory_row, "inventory")
    db_manager.clean_table("inventory")

    with db_manager.conn.cursor() as cursor:
        cursor.execute("SELECT COUNT(*) FROM inventory;")
        query_result = cursor.fetchone()[0]
        assert query_result == 0


def test_insert_data(db_manager):  # pylint: disable=redefined-outer-name
    """
    Test case for the insert_data method of the DatabaseManager class.
    """

    db_manager.create_table()
    inventory_row = [
        ("Store1", "ProductA", datetime.strptime(
            "2024-01-01", "%Y-%m-%d").date(), 100)
    ]
    db_manager.insert_data(inventory_row, "inventory")

    with db_manager.conn.cursor() as cursor:
        cursor.execute("SELECT COUNT(*) FROM inventory;")
        query_result = cursor.fetchone()[0]
        assert query_result == 1

        cursor.execute(
            "SELECT PointOfSale, Product, Date, Stock FROM inventory;")
        query_result = cursor.fetchone()
        assert query_result == inventory_row[0]
