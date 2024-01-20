# Data Optimization Project

## Description
This project is a Python application for reading data from a CSV file and loading it into a PostgreSQL database, optimizing performance and minimizing resource consumption.

## Technologies Used
- **Python**: Programming language used for application development.
- **Pandas**: Python library for data manipulation and analysis.
- **Psycopg2**: PostgreSQL database adapter for the Python programming language.
- **PostgreSQL**: Relational database management system.

## How to Run
To run this project, follow these steps:

0. **CSV File Setup**:
- Create a CSV file separated by ; (semicolon) with the following columns inside on a `data` folder on the root of the project:
    - `PointOfSale`: string
    - `Product`: string
    - `Date`: date
    - `Stock`: integer


1. **Clone the Repository**:
    - Open the command line and navigate to the directory where you want to clone the repository.
    - Run the following command:
        ```
        git clone https://github.com/EdinsonRequena/data_optimization_test.git
        ```

2. **Install Dependencies**:
    - Install [Pipenv](https://pypi.org/project/pipenv/).
    - Navigate to the project's root directory.
    - Run the following command:
        ```
        pipenv install Pipfile
        ```
    - Activate the virtual environment by running the following command:
        ```
        pipenv shell
        ```

3. **Database Setup**:
- Ensure PostgreSQL is installed and running.
- Create a database for the project.

4. **Setup `.env` File**:
Create a `.env` file in the root of the project with the following variables:
```
DB_NAME=your_database_name
DB_USER=your_username
DB_PASS=your_password
DB_HOST=localhost (or your database host)
DB_PORT=5432 (or your database port)
```

5. **Run the Application**:
- Navigate to the project's root directory.
- Run the following command:
    ```
    pipenv run python main.py
    ```