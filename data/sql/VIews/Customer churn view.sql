CREATE VIEW cohort_retention AS
WITH first_purchase AS (
SELECT 
customer_id,
MIN(order_date) first_order_date
FROM orders
GROUP BY customer_id
),

cohort AS (
SELECT 
DATE_FORMAT(fp.first_order_date,'%Y-%m') cohort_month,
DATE_FORMAT(o.order_date,'%Y-%m') order_month,
COUNT(DISTINCT o.customer_id) customers
FROM orders o
JOIN first_purchase fp
ON o.customer_id = fp.customer_id
GROUP BY cohort_month, order_month
)

SELECT 
cohort_month,
order_month,
customers,
customers /
FIRST_VALUE(customers) OVER (
PARTITION BY cohort_month 
ORDER BY order_month
) AS retention_rate
FROM cohort;