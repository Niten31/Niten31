import pandas as pd

# Load CSV or DataFrame from extraction step
df = pd.read_csv("snacks_100_products.csv")

# 1. Drop rows where product name or energy is missing
df.dropna(subset=["product_name", "energy_kcal"], inplace=True)

# 2. Clean brand names
df["brands"] = df["brands"].fillna("Unknown").str.title()

# 3. Convert countries from list to string
df["countries"] = df["countries"].astype(str).str.replace("[", "").str.replace("]", "").str.replace("'", "")

# 4. Normalize quantity field (extract numeric value and unit)
df["quantity_value"] = df["quantity"].str.extract(r'(\d+\.?\d*)')
df["quantity_unit"] = df["quantity"].str.extract(r'([a-zA-Z]+)')

# 5. Standardize column names for SQL
df.columns = df.columns.str.lower().str.replace(" ", "_")

# 6. Preview cleaned DataFrame
print(df.head())

#saving the transform data
df.to_csv("transformed_snacks.csv", index=False)
print("✅ Data saved as transformed_snacks.csv")
