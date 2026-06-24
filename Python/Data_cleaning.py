import pandas as pd
import numpy as np
import os

RAW_PATH = r"D:\python project files\E-commerce Revenue Intelligence and Customer Analytics\data\raw"
CLEAN_PATH = r"D:\python project files\E-commerce Revenue Intelligence and Customer Analytics\data\cleaned"

os.makedirs(CLEAN_PATH, exist_ok=True)

def clean_orders(df):
    df = df.drop_duplicates()
    df = df.dropna()
    df['discount'] = df['discount'].fillna(0)

    df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')
    df['sales'] = df['sales'].astype(float)
    df['profit'] = df['profit'].astype(float)

    df = df[df['sales'] > 0]
    df = df[df['quantity'] > 0]
    df = df[(df['discount'] >= 0) & (df['discount'] <= 1)]
    df = df[df['sales'] < df['sales'].quantile(0.99)]

    return df

def clean_generic(df):
    df = df.drop_duplicates()
    df = df.dropna()
    return df

def clean_data():
    # Load raw files
    orders = pd.read_csv(os.path.join(RAW_PATH, "orders.csv"))
    customers = pd.read_csv(os.path.join(RAW_PATH, "customers.csv"))
    products = pd.read_csv(os.path.join(RAW_PATH, "products.csv"))
    returns = pd.read_csv(os.path.join(RAW_PATH, "returns.csv"))

    # Clean
    clean_orders_df = clean_orders(orders)
    clean_customers_df = clean_generic(customers)
    clean_products_df = clean_generic(products)
    clean_returns_df = clean_generic(returns)

    # Save
    clean_orders_df.to_csv(os.path.join(CLEAN_PATH, "clean_orders.csv"), index=False)
    clean_customers_df.to_csv(os.path.join(CLEAN_PATH, "clean_customers.csv"), index=False)
    clean_products_df.to_csv(os.path.join(CLEAN_PATH, "clean_products.csv"), index=False)
    clean_returns_df.to_csv(os.path.join(CLEAN_PATH, "clean_returns.csv"), index=False)

    print("✅ Cleaned datasets saved successfully!")

# ===================================
# Runner
# ===================================
if __name__ == "__main__":
    clean_data()

