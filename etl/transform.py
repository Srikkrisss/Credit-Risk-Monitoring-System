import pandas as pd
from pathlib import Path

from logger import logger

RAW_PATH = Path("data/raw")
PROCESSED_PATH = Path("data/processed")

PROCESSED_PATH.mkdir(parents=True, exist_ok=True)


def transform_data():

    try:

        csv_files = list(RAW_PATH.glob("*.csv"))

        for file in csv_files:

            df = pd.read_csv(file)

            # Remove duplicate rows
            df.drop_duplicates(inplace=True)

            # Fill missing values
            df.fillna("Unknown", inplace=True)

            # Remove leading/trailing spaces
            df.columns = df.columns.str.strip()

            output = PROCESSED_PATH / file.name

            df.to_csv(output, index=False)

            logger.info(f"{file.name}: {len(df)} rows transformed")

        print("Transformation Successful")

    except Exception as e:

        logger.error(str(e))

        print(e)


if __name__ == "__main__":

    transform_data()