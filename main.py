import time

from dotenv import load_dotenv

from app.csv_handler.processor import read_csv
from app.database.manager import DatabaseManager
from app.utils.logger_config import configure_logger

logger = configure_logger()


def main():
    """
    This function is the entry point of the application.
    It performs the following steps:
    1. Loads the .env file.
    2. Connects to the database and creates a table.
    3. Reads the CSV file.
    4. Prepares the data to be inserted into the database.
    5. Cleans the table.
    6. Inserts the data into the table.
    7. Prints the total execution time.
    """
    start_time = time.time()

    logger.info("Loading .env file...")
    load_dotenv()
    logger.info(".env loaded successfully.")

    with DatabaseManager() as db_manager:
        logger.info("Connecting to database and creating table...")
        db_manager.create_table()
        logger.info("Table created successfully.")

        logger.info("Reading CSV file...")
        csv_data = read_csv('data/Stock.csv')
        logger.info("CSV file read successfully.")

        logger.info("Preparing data to insert...")
        data_to_insert = [
            (row['PointOfSale'], row['Product'], row['Date'], row['Stock'])
            for index, row in csv_data.iterrows()
        ]
        logger.info("Data prepared.")

        logger.info("Cleaning table...")
        db_manager.clean_table('inventory')
        logger.info("Table cleaned.")

        logger.info("Inserting data...")
        db_manager.insert_data(data_to_insert, 'inventory')
        logger.info("Data inserted successfully.")

    end_time = time.time()
    logger.info("Total execution time: %s seconds", end_time - start_time)


if __name__ == "__main__":
    main()
