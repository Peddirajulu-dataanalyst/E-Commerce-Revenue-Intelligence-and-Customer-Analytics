#Region Performance
CREATE VIEW region_performance as 
select 
region,
sum(sales) revenue,
sum(profit) profit
from orders
group by region
order by revenue desc 