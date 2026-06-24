import pandas as pd
import numpy as np
from faker import Faker
import os

fake = Faker()

# Base folder
BASE_PATH = r"D:\python project files\E-commerce Revenue Intelligence and Customer Analytics\data\raw"
os.makedirs(BASE_PATH, exist_ok=True)

def generate_customers(n_customers=10000):
    customers = pd.DataFrame({
        "customer_id": range(1, n_customers+1),
        "signup_date": [fake.date_between(start_date='-3y', end_date='today') for _ in range(n_customers)],
        "segment": np.random.choice(["Consumer","Corporate","Home Office"], n_customers),
        "city": [fake.city() for _ in range(n_customers)],
        "state": [fake.state() for _ in range(n_customers)],
        "country": "USA"
    })
    customers.to_csv(os.path.join(BASE_PATH, "customers.csv"), index=False)
    print("customers.csv created")

def generate_products(n_products=500):
    categories = ["Furniture","Technology","Office Supplies"]
    subcats = ["Chairs","Phones","Binders","Tables","Accessories"]
    subcat_values = np.random.choice(subcats, n_products)

    products = pd.DataFrame({
        "product_id": range(1, n_products+1),
        "category": np.random.choice(categories, n_products),
        "subcategory": np.random.choice(subcats, n_products),
        "product_name": [f"{fake.color_name()} {sub} {fake.word().capitalize()}" for sub in subcat_values],
        "cost": np.random.uniform(10,300,n_products).round(2),
    })
    products["price"] = (products["cost"] * np.random.uniform(1.2,1.8,n_products)).round(2)
    products.to_csv(os.path.join(BASE_PATH, "products.csv"), index=False)
    print("products.csv created")

def generate_orders(n_orders=200000):
    sales_vals = np.random.uniform(20,500,n_orders).round(2)
    orders = pd.DataFrame({
        "order_id": range(1,n_orders+1),
        "order_date": [fake.date_between(start_date='-2y', end_date='today') for _ in range(n_orders)],
        "customer_id": np.random.randint(1,10001,n_orders),
        "product_id": np.random.randint(1,501,n_orders),
        "quantity": np.random.randint(1,5,n_orders),
        "sales": sales_vals,
        "discount": np.random.uniform(0,0.3,n_orders).round(2),
        "profit": (sales_vals * np.random.uniform(0.05,0.3,n_orders)).round(2),
        "region": np.random.choice(["West","East","Central","South"], n_orders),
        "channel": np.random.choice(["Online","Retail"], n_orders)
    })
    orders.to_csv(os.path.join(BASE_PATH, "orders.csv"), index=False)
    print("orders.csv created")

def generate_returns(n_returns=15000):
    returns = pd.DataFrame({
        "order_id": np.random.randint(1,200001,n_returns),
        "return_flag": "Yes",
        "return_reason": np.random.choice(
            ["Damaged","Wrong Item","Late Delivery","Customer Changed Mind"],
            n_returns
        )
    })
    returns.to_csv(os.path.join(BASE_PATH, "returns.csv"), index=False)
    print("returns.csv created")

if __name__ == "__main__":
    generate_customers()
    generate_products()
    generate_orders()
    generate_returns()
    print("All datasets created successfully!")
