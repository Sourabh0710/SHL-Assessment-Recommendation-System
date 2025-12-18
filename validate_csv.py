import pandas as pd

df = pd.read_csv("shl_catalog.csv")

print("Columns:", list(df.columns))
print("Total rows:", len(df))

required = {"assessment_name", "description", "test_type", "url"}
missing = required - set(df.columns)

if missing:
    print("Missing columns:", missing)
else:
    print("All columns are present")

invalid = df[~df["test_type"].isin(["K", "A", "P"])]
print("Invalid test_type rows:", len(invalid))

print("Empty assessment_name:", df["assessment_name"].isna().sum())
print("Empty description:", df["description"].isna().sum())
print("Empty url:", df["url"].isna().sum())
