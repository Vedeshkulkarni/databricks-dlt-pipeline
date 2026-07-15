# Databricks Delta Live Tables (DLT) ETL Pipeline

## Overview
This project demonstrates an end-to-end ETL pipeline built using Databricks Delta Live Tables (DLT) and PySpark. The pipeline follows the Medallion Architecture (Bronze, Silver, and Gold) to process sales data efficiently.

## Architecture

Bronze → Silver → Gold

- Bronze Layer: Raw data ingestion
- Silver Layer: Data cleaning and transformation
- Gold Layer: Dimension and Fact table creation using SCD Type 2

## Technologies Used

- Databricks
- Delta Live Tables (DLT)
- PySpark
- Delta Lake
- Git
- GitHub

## Project Structure

```
dlt_end_to_end/
├── bronze/
│   └── ingestion.py
├── silver/
│   ├── customers_silver.py
│   ├── products_silver.py
│   ├── sales_silver.py
│   └── stores_silver.py
├── gold/
│   ├── dim_customers.py
│   ├── dim_products.py
│   ├── dim_stores.py
│   └── facts_sales.py
└── manifest.mf
```

## Features

- End-to-end ETL pipeline
- Medallion Architecture
- Streaming tables
- Auto Loader
- Data validation and transformation
- SCD Type 2 implementation
- Git version control

## Screenshots

Project screenshots are available in the `screenshots` folder.

## Author

**Vedesh Kulkarni**
