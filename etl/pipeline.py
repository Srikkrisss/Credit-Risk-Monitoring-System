from etl.extract import extract_data
from etl.transform import transform_data
from etl.load import load_data


def run_pipeline():

    print("\n========== ETL PIPELINE STARTED ==========\n")

    extract_data()

    transform_data()

    load_data()

    print("\n========== ETL PIPELINE COMPLETED ==========\n")


if __name__ == "__main__":

    run_pipeline()