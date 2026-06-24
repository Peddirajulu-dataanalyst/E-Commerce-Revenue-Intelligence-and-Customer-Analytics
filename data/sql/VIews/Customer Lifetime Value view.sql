#Customer Lifetime Value (CLV)
CREATE VIEW customer_lifetime_value as 
select 
customer_id,
sum(sales) as clv,
count(order_id) as total_orders
from orders 
GROUP BY CUSTOMER_ID
ORDER BY clv DESC