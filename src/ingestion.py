import os

import pandas as pd

from config import RAW_DATA, REPORTS
from logger import logger

os.makedirs(REPORTS, exist_ok=True)

FILES = {
    "Listings": "listings.csv",
    "Calendar": "calendar.csv",
    "Reviews": "reviews.csv",
    "Neighbourhoods": "neighbourhoods.csv"
}

def load_dataset(file_name):
    path = os.path.join(RAW_DATA, file_name)

    if not os.path.exists(path):
        logger.error("%s not found.", file_name)
        return None

    df = pd.read_csv(path)

    logger.info("Loaded %s", file_name)
    return df

datasets = {}

for name, file in FILES.items():
    datasets[name] = load_dataset(file)

logger.info("==============================")
logger.info("DATASET SUMMARY")
logger.info("==============================")

for name, df in datasets.items():

    if df is not None:
        logger.info("%s", name)
        logger.info("%s", "-" * 30)
        logger.info("Rows    : %s", df.shape[0])
        logger.info("Columns : %s", df.shape[1])

def profile_dataset(name, df):

    report_path = os.path.join(REPORTS, f"{name}_profile.txt")

    with open(report_path, "w", encoding="utf-8") as file:

        file.write(f"{name}\n")
        file.write("=" * 60 + "\n\n")

        file.write("Shape\n")
        file.write(str(df.shape))
        file.write("\n\n")

        file.write("Data Types\n")
        file.write(str(df.dtypes))
        file.write("\n\n")

        file.write("Missing Values\n")
        file.write(str(df.isnull().sum()))
        file.write("\n\n")

        file.write("Duplicate Rows\n")
        file.write(str(df.duplicated().sum()))
        file.write("\n\n")

        file.write("Summary Statistics\n")
        file.write(str(df.describe(include="all")))

    logger.info("Profile saved for %s", name)

for name, df in datasets.items():

    if df is not None:
        profile_dataset(name, df)

