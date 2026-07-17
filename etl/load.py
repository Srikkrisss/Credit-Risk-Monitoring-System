from pathlib import Path

from logger import logger

PROCESSED_PATH = Path("data/processed")


def load_data():

    try:

        csv_files = list(PROCESSED_PATH.glob("*.csv"))

        print()

        print("Processed Files")

        print("--------------------")

        for file in csv_files:

            print(file.name)

            logger.info(f"{file.name} ready for loading")

        print()

        print("Load Successful")

    except Exception as e:

        logger.error(str(e))

        print(e)


if __name__ == "__main__":

    load_data()