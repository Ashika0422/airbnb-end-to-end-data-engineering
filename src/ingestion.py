import os
import pandas as pd

# -----------------------------
# Project Paths
# -----------------------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

RAW_DATA = os.path.join(BASE_DIR, "data", "raw")

# -----------------------------
# File Names
# -----------------------------
FILES = {
    "Listings": "listings.csv",
    "Calendar": "calendar.csv",
    "Reviews": "reviews.csv",
    "Neighbourhoods": "neighbourhoods.csv"
}

def load_dataset(file_name):
    path = os.path.join(RAW_DATA, file_name)

    if not os.path.exists(path):
        print(f"[ERROR] {file_name} not found.")
        return None

    df = pd.read_csv(path)

    print(f"[SUCCESS] Loaded {file_name}")
    return df

datasets = {}

for name, file in FILES.items():
    datasets[name] = load_dataset(file)

print("\n==============================")
print("DATASET SUMMARY")
print("==============================")

for name, df in datasets.items():

    if df is not None:
        print(f"\n{name}")
        print("-" * 30)
        print(f"Rows    : {df.shape[0]}")
        print(f"Columns : {df.shape[1]}")

def profile_dataset(name, df):

    report_path = os.path.join(BASE_DIR, "reports", f"{name}_profile.txt")

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

    print(f"[SUCCESS] Profile saved for {name}")

for name, df in datasets.items():

    if df is not None:
        profile_dataset(name, df)

