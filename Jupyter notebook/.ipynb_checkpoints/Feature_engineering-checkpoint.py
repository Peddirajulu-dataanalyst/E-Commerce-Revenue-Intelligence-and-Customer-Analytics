import pandas as pd
import os

RAW_PATH   = r"D:\python project files\E-commerce Revenue Intelligence and Customer Analytics\data\raw"
CLEAN_PATH = r"D:\python project files\E-commerce Revenue Intelligence and Customer Analytics\data\cleaned"

os.makedirs(CLEAN_PATH, exist_ok=True)

def run_feature_engineering():
    # Step 1: Load raw data
    orders    = pd.read_csv(os.path.join(CLEAN_PATH, "orders.csv"))
    customers = pd.read_csv(os.path.join(CLEAN_PATH, "customers.csv"))
    products  = pd.read_csv(os.path.join(CLEAN_PATH, "products.csv"))
    returns   = pd.read_csv(os.path.join(CLEAN_PATH, "returns.csv"))

    # Step 2: Time features
    orders['order_date']   = pd.to_datetime(orders['order_date'], errors='coerce')
    orders['order_month']  = orders['order_date'].dt.to_period('M')
    orders['order_year']   = orders['order_date'].dt.year

    # Step 3: Profit margin
    orders['profit_margin'] = orders['profit'] / orders['sales']

    # Step 4: Discount bucket
    orders['discount_bucket'] = pd.cut(
        orders['discount'],
        bins=[0,0.1,0.2,0.3,1],
        labels=['Low','Medium','High','Very High']
    )

    # Step 5: Customer revenue
    customer_revenue = orders.groupby('customer_id')['sales'].sum()
    orders['customer_revenue'] = orders['customer_id'].map(customer_revenue)

    # Step 6: Order frequency
    order_freq = orders.groupby('customer_id').size()
    orders['order_frequency'] = orders['customer_id'].map(order_freq)

    # Step 7: Recency
    last_date = orders['order_date'].max()
    recency = orders.groupby('customer_id')['order_date'].max()
    recency = (last_date - recency).dt.days
    orders['recency'] = orders['customer_id'].map(recency)

    # Step 8: RFM summary
    rfm = orders.groupby('customer_id').agg({
        'order_date':'max',
        'order_id':'count',
        'sales':'sum'
    }).reset_index()
    rfm.rename(columns={'order_date':'last_order_date',
                        'order_id':'order_count',
                        'sales':'total_sales'}, inplace=True)

    # Save engineered datasets
    orders.to_csv(os.path.join(CLEAN_PATH, "clean_orders_f.csv"), index=False)
    customers.to_csv(os.path.join(CLEAN_PATH, "clean_customers_f.csv"), index=False)
    products.to_csv(os.path.join(CLEAN_PATH, "clean_products_f.csv"), index=False)
    returns.to_csv(os.path.join(CLEAN_PATH, "clean_returns_f.csv"), index=False)
    rfm.to_csv(os.path.join(CLEAN_PATH, "rfm_summary_f.csv"), index=False)

    print("✅ Feature engineering completed. Files saved in:", CLEAN_PATH)

# ===================================
# Runner pipeline
# ===================================
if __name__ == "__main__":
    run_feature_engineering()
