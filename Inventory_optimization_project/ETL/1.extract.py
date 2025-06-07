import requests
import pandas as pd

# Base API URL for category 'snacks'
url = "https://world.openfoodfacts.org/category/snacks.json"

# Request the data
response = requests.get(url)

# Check status and parse
if response.status_code == 200:
    data = response.json()
    products = data.get("products", [])[:100]  # Limit to 100 products

    # Extract useful fields
    extracted_data = []
    for p in products:
        extracted_data.append({
            "product_name": p.get("product_name"),
            "brands": p.get("brands"),
            "countries": p.get("countries_tags"),
            "quantity": p.get("quantity"),
            "nutriscore_grade": p.get("nutriscore_grade"),
            "ingredients_text": p.get("ingredients_text"),
            "energy_kcal": p.get("nutriments", {}).get("energy-kcal_100g"),
        })

    # Load into a DataFrame
    df = pd.DataFrame(extracted_data)
    print(df.head())

    # Optional: Save to CSV
    df.to_csv("snacks_100_products.csv", index=False)
    print("✅ Saved to snacks_100_products.csv")

else:
    print(f"❌ Failed to fetch data: {response.status_code}")
