from extract import extract_data
from transform import transform_data
from load import load_data

from logger import logger


def run_pipeline():

    logger.info("ETL Pipeline Started")

    print()

    print("==============================")

    print(" CREDIT RISK ETL PIPELINE ")

    print("==============================")

    print()

    extract_data()

    transform_data()

    load_data()

    logger.info("ETL Pipeline Completed")

    print()

    print("==============================")

    print(" ETL COMPLETED ")

    print("==============================")


if __name__ == "__main__":

    run_pipeline()