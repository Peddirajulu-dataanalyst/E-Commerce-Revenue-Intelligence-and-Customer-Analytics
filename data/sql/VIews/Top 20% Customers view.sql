#Top 20% Customers (Revenue Concentration)
CREATE VIEW top_20_customers as 
select *
from (
select
customer_id,
sum(sales) revenue,
NTILE(5) OVER (ORDER BY	sum(sales) DESC) as bucket
FROM orders
GROUP BY customer_id
)t
where bucket = 1;