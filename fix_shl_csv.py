import pandas as pd

df = pd.read_csv("shl_catalogue.csv")

print("Original columns:", list(df.columns))
print("Original rows:", len(df))

df = df.rename(columns={
    "name": "assessment_name"
})

df["description"] = (
    df["assessment_name"].fillna("") +
    " assessment provided by SHL to evaluate relevant skills."
)

def normalize_test_type(x):
    if pd.isna(x):
        return "K"
    x = str(x).upper()
    if x in ["P", "PERSONALITY"]:
        return "P"
    if x in ["A", "ABILITY", "COGNITIVE"]:
        return "A"
    return "K"

df["test_type"] = df["test_type"].apply(normalize_test_type)

df = df[[
    "assessment_name",
    "description",
    "test_type",
    "url"
]]

df = df.drop_duplicates(subset=["assessment_name"])
df = df.dropna(subset=["assessment_name", "url"])

print("Cleaned rows:", len(df))
print("Test type counts:\n", df["test_type"].value_counts())

df.to_csv("shl_catalog.csv", index=False)
print("shl_catalog.csv created successfully")
