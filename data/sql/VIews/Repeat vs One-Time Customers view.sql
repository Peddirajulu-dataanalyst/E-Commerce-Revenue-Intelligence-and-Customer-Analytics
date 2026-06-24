#Repeat vs One-Time Customers
CREATE VIEW one_time_customers as 
select 
CASE
WHEN order_count = 1 THEN 'One-time'
ELSE 'Repeat'
END AS customer_type,
count(*) customers
FROM ( 
select customer_id,COUNT(*) order_count
FROM orders
GROUP BY customer_id
)t
GROUP BY customer_type