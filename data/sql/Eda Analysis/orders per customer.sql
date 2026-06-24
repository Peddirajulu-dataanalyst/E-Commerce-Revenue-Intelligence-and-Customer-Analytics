#orders per customer
select 
count(*) orders,
count(DISTINCT customer_id) customers,
count(*)/count(DISTINCT customer_id) avg_orders_per_customer
from orders;