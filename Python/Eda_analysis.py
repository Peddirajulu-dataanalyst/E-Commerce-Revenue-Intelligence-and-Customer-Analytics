import pandas as pd
import os
import matplotlib.pyplot as plt

# Paths
CLEAN_PATH = r"D:\python project files\E-commerce Revenue Intelligence and Customer Analytics\data\cleaned"
EDA_PATH   = r"D:\python project files\E-commerce Revenue Intelligence and Customer Analytics\data\eda"

# Ensure EDA folder exists
os.makedirs(EDA_PATH, exist_ok=True)

def run_eda():
    # Step 1: Load cleaned data
    orders    = pd.read_csv(os.path.join(CLEAN_PATH, "clean_orders.csv"))
    customers = pd.read_csv(os.path.join(CLEAN_PATH, "clean_customers.csv"))
    products  = pd.read_csv(os.path.join(CLEAN_PATH, "clean_products.csv"))
    returns   = pd.read_csv(os.path.join(CLEAN_PATH, "clean_returns.csv"))

    # Step 2–5: Dataset shapes
    print("Customers shape:", customers.shape)
    print("Returns shape:", returns.shape)
    print("Products shape:", products.shape)
    print("Orders shape:", orders.shape)

    # Step 6: Data types
    print("\nOrders info:")
    print(orders.info())

    # Step 7: Missing values
    print("\nMissing values in orders:")
    print(orders.isnull().sum())

    # Step 8: Summary statistics
    print("\nOrders summary statistics:")
    print(orders.describe())

    # Step 9: Profit distribution
    plt.figure()
    orders['profit'].hist()
    plt.title("Profit Distribution")
    plt.xlabel("Profit")
    plt.ylabel("Frequency")
    plt.savefig(os.path.join(EDA_PATH, "profit_distribution.png"))
    plt.close()

    # Step 10: Revenue distribution
    plt.figure()
    orders['sales'].hist()
    plt.title("Revenue Distribution")
    plt.xlabel("Sales")
    plt.ylabel("Frequency")
    plt.savefig(os.path.join(EDA_PATH, "revenue_distribution.png"))
    plt.close()

    # Step 11: Orders per customer
    print("\nOrders per customer stats:")
    print(orders.groupby('customer_id').size().describe())

    # Step 12: Category revenue
    merged = orders.merge(products, on='product_id')
    print("\nCategory revenue:")
    print(merged.groupby('category')['sales'].sum())

    # Step 13: Channel distribution
    print("\nChannel distribution:")
    print(orders['channel'].value_counts())

    print("\n✅ EDA completed. Plots saved in:", EDA_PATH)

# ===================================
# Runner pipeline
# ===================================
if __name__ == "__main__":
    run_eda()
