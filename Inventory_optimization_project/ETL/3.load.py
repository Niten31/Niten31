import pandas as pd
import mysql.connector
import numpy as np

# Load transformed data
df = pd.read_csv("transformed_snacks.csv")

# Replace NaN with None
df = df.replace({np.nan: None})

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password@1131",
    database="inventory_etl"
)

cursor = conn.cursor()

# Insert each row
for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO snacks 
        (product_name, brands, countries, quantity_value, quantity_unit, nutriscore_grade, energy_kcal)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, (
        row['product_name'],
        row['brands'],
        row['countries'],
        row['quantity_value'],
        row['quantity_unit'],
        row['nutriscore_grade'],
        row['energy_kcal']
    ))

conn.commit()
cursor.close()
conn.close()

print("✅ Data loaded successfully into MySQL!")
