import time
import pandas as pd
from pathlib import Path
from sqlalchemy import create_engine
from urllib.parse import quote_plus

from config import *
from logger import logger

# Create raw data directory if it doesn't exist
RAW_PATH = Path("data/raw")
RAW_PATH.mkdir(parents=True, exist_ok=True)


def extract_data():
    """
    Extract all tables from SQL Server
    and save them as CSV files in data/raw.
    """

    start_time = time.time()
    total_rows = 0
    engine = None

    try:

        # SQL Server Connection String
        connection_string = (
            f"DRIVER={{{DRIVER}}};"
            f"SERVER={SERVER};"
            f"DATABASE={DATABASE};"
            f"Trusted_Connection={TRUSTED_CONNECTION};"
            "TrustServerCertificate=yes;"
        )

        # Create SQLAlchemy Engine
        engine = create_engine(
            f"mssql+pyodbc:///?odbc_connect={quote_plus(connection_string)}"
        )

        tables = [
            "Customers",
            "Branches",
            "Loans",
            "LoanOfficers",
            "CreditScores",
            "FinancialStatements",
            "Collateral",
            "Repayments"
        ]

        print("\n========== EXTRACTION STARTED ==========\n")

        for table in tables:

            query = f"SELECT * FROM {table}"

            df = pd.read_sql(query, engine)

            df.to_csv(
                RAW_PATH / f"{table}.csv",
                index=False
            )

            rows = len(df)
            total_rows += rows

            logger.info(f"{table} exported successfully ({rows} rows)")

            print(f"✔ {table:<22} {rows} rows")

        end_time = time.time()

        print("\n========== EXTRACTION COMPLETED ==========")
        print(f"Tables Exported : {len(tables)}")
        print(f"Total Rows      : {total_rows}")
        print(f"Execution Time  : {end_time - start_time:.2f} seconds\n")

        logger.info(
            f"Extraction Completed | Tables={len(tables)} | Rows={total_rows}"
        )

    except Exception as e:

        logger.error(f"Extraction Failed : {str(e)}")
        print("\nExtraction Failed")
        print(e)

    finally:

        if engine:
            engine.dispose()
            logger.info("Database Connection Closed")


if __name__ == "__main__":
    extract_data()