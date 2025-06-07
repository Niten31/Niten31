# 🧠 Smart Inventory Insights: ETL Project for Business Growth

## 🚀 Overview
This project demonstrates a complete **ETL (Extract, Transform, Load)** pipeline using:
- Real-world product data from the **Open Food Facts API**
- Data processing in **Python**
- Storage and querying using **MySQL**
- Visualization and business insights in **Power BI**

It aims to improve inventory decisions by analyzing product health scores and performance across brands and countries.

---

## 🔧 Technologies Used

| Stack          | Tool                          |
|----------------|-------------------------------|
| Extraction     | Open Food Facts API           |
| Transformation | Python (Pandas, Requests)     |
| Load           | MySQL                         |
| Visualization  | Power BI                      |
| Version Control| Git & GitHub                  |

---

inventory-insights-etl-project/
├── ETL/                        # Python scripts for data pipeline
│   ├── extract.py              # Extracts data from Open Food Facts API
│   ├── transform.py            # Cleans and transforms the data
│   └── load.py                 # Loads data into MySQL database
│
├── dashboard/                  # Power BI dashboard
│   └── power_bi_dashboard.pbix
│
├── sql/                        # SQL schema
│   └── create_table.sql
│
├── README.md                   # Project overview and instructions
