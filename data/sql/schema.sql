CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    signup_date DATE,
    segment VARCHAR(50),
    city VARCHAR(50),
    state VARCHAR(50),
    country VARCHAR(50)
);

CREATE TABLE products (
    product_id INT PRIMARY KEY,
    category VARCHAR(50),
    subcategory VARCHAR(50),
    product_name VARCHAR(100),
    cost DECIMAL(10,2),
    price DECIMAL(10,2)
);

CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    order_date DATE,
    customer_id INT,
    product_id INT,
    quantity INT,
    sales DECIMAL(10,2),
    discount DECIMAL(5,2),
    profit DECIMAL(10,2),
    region VARCHAR(50),
    channel VARCHAR(50),

    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

CREATE TABLE returns (
    return_id INT PRIMARY KEY AUTO_INCREMENT,
    order_id INT,
    return_flag VARCHAR(10),
    return_reason VARCHAR(100),

    FOREIGN KEY (order_id) REFERENCES orders(order_id)
);