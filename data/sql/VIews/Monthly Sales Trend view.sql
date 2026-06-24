#Monthly Sales Trend
CREATE VIEW month_sales_trend as 
select 
DATE_Format(order_date,'%Y-%m') as month,
sum(sales) as revenue,
sum(profit) as profit
from orders
group by month
order by month;