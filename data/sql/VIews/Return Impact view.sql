create view return_impact as
SELECT 
r.return_reason,
COUNT(distinct r.order_id) AS total_returns,
COUNT(r.order_id) / (SELECT COUNT(*) FROM orders) AS return_rate,
SUM(o.sales) AS lost_revenue,
SUM(o.profit) AS lost_profit
FROM orders o
LEFT JOIN returns r
ON o.order_id = r.order_id
WHERE r.return_reason IS NOT NULL
GROUP BY r.return_reason;