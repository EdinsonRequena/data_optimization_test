import os
from datetime import date
from typing import List, Tuple, Optional

import psycopg2
from psycopg2 import extras, sql
from psycopg2.extensions import connection as pg_connection


InventoryRowType = List[Tuple[str, str, date, int]]


class DatabaseManager:
    """
    A class that manages the database connection and operations.

    Attributes:
        conn (Optional[pg_connection]): The database connection object.

    Methods:
        __init__(): Initializes the DatabaseManager object.
        __enter__(): Establishes a database connection.
        __exit__(): Closes the database connection.
        create_table(): Creates a table in the database.
        clean_table(table_name: str): Cleans (truncates) a table in the database.
        insert_data(inventory_row: InventoryRowType, table_name: str): Inserts data into a table in the database.
    """

    def __init__(self):
        self.conn: Optional[pg_connection] = None

    def __enter__(self) -> 'DatabaseManager':
        """
        Context manager method that establishes a connection to the database.

        Returns:
            DatabaseManager: The current instance of the DatabaseManager class.
        """
        self.conn = psycopg2.connect(
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASS"),
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT")
        )
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()

    def create_table(self):
        """
        Creates a table named 'inventory' in the database if it doesn't already exist.
        The table has the following columns:
        - PointOfSale: VARCHAR(255)
        - Product: VARCHAR(255)
        - Date: DATE
        - Stock: INT
        """

        create_table_query = """
            CREATE TABLE IF NOT EXISTS inventory (
                PointOfSale VARCHAR(255),
                Product VARCHAR(255),
                Date DATE,
                Stock INT
            );
        """
        with self.conn.cursor() as cursor:
            cursor.execute(create_table_query)
            self.conn.commit()

    def clean_table(self, table_name: str):
        """
        Cleans (truncates) the specified table in the database.

        Args:
            table_name (str): The name of the table to be cleaned.
        """
        with self.conn.cursor() as cursor:
            query = sql.SQL("TRUNCATE TABLE {} RESTART IDENTITY CASCADE;").format(
                sql.Identifier(table_name))
            cursor.execute(query)
            self.conn.commit()

    def insert_data(self, inventory_row: InventoryRowType, table_name: str):
        """
        Inserts data into the specified table in the database.

        Args:
            inventory_row (InventoryRowType): The inventory row data to be inserted.
            table_name (str): The name of the table to insert the data into.
        """
        with self.conn.cursor() as cursor:
            insert_query = f"""
                INSERT INTO {table_name} (PointOfSale, Product, Date, Stock)
                VALUES %s
            """
            extras.execute_values(
                cursor,
                insert_query,
                inventory_row, page_size=2000
            )
            self.conn.commit()
