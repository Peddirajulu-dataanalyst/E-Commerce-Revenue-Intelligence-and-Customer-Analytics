import pandas as pd
import numpy as np

print("Loading datasets...")

# Load CSV files
orders = pd.read_csv("orders.csv")
customers = pd.read_csv("customers.csv")
products = pd.read_csv("products.csv")
returns = pd.read_csv("returns.csv")


# Generic cleaning function
def clean_data(df):

    # Remove duplicate rows
    df = df.drop_duplicates()

    # Clean column names
    df.columns = df.columns.str.strip()

    # Standardize text columns
    for col in df.select_dtypes(include='object').columns:
        df[col] = df[col].astype(str).str.strip()

    # Replace blank spaces with NaN
    df = df.replace(r'^\s*$', np.nan, regex=True)

    # Fill missing numeric values with median
    numeric_cols = df.select_dtypes(include=np.number).columns
    for col in numeric_cols:
        df[col] = df[col].fillna(df[col].median())

    # Fill missing text values
    text_cols = df.select_dtypes(include='object').columns
    for col in text_cols:
        df[col] = df[col].fillna("Unknown")

    return df


print("Cleaning datasets...")

# Apply cleaning
orders = clean_data(orders)
customers = clean_data(customers)
products = clean_data(products)
returns = clean_data(returns)


# Date cleaning
if "order_date" in orders.columns:
    orders["order_date"] = pd.to_datetime(
        orders["order_date"],
        errors="coerce"
    )


# Remove invalid sales records
if "sales" in orders.columns:
    orders = orders[orders["sales"] > 0]


# Remove sales outliers (optional advanced cleaning)
if "sales" in orders.columns:

    Q1 = orders["sales"].quantile(0.25)
    Q3 = orders["sales"].quantile(0.75)

    IQR = Q3 - Q1

    lower_limit = Q1 - (1.5 * IQR)
    upper_limit = Q3 + (1.5 * IQR)

    orders = orders[
        (orders["sales"] >= lower_limit) &
        (orders["sales"] <= upper_limit)
    ]


print("Saving cleaned files...")

# Save cleaned files
orders.to_csv("clean_orders.csv", index=False)
customers.to_csv("clean_customers.csv", index=False)
products.to_csv("clean_products.csv", index=False)
returns.to_csv("clean_returns.csv", index=False)

print("Data cleaning completed successfully.")