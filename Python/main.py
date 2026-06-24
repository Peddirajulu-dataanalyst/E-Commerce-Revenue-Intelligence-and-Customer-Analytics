from Data_generation import generate_customers, generate_products, generate_orders, generate_returns
from Data_Cleaning import clean_data
from Eda_Analysis import run_eda
from feature_engineering import run_feature_engineering
import logging

# Configure logging globally
logging.basicConfig(
    filename="pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def main():
    logging.info("Pipeline Started")

    # Data generation
    generate_customers()
    logging.info("Customers generated")

    generate_products()
    logging.info("Products generated")

    generate_orders()
    logging.info("Orders generated")

    generate_returns()
    logging.info("Returns generated")

    # Data cleaning
    clean_data()
    logging.info("Cleaning completed")

    # EDA
    run_eda()
    logging.info("EDA completed")

    # Feature engineering
    run_feature_engineering()
    logging.info("Feature Engineering completed")

    logging.info("Pipeline Finished Successfully")
    print("✅ Project completed successfully")

# ===================================
# Runner
# ===================================
if __name__ == "__main__":
    main()
