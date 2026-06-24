#Product Profitability
CREATE VIEW product_profitability as
select 
product_id,
sum(sales) revenue,
sum(profit) profit
from orders
group by product_id
order by profit ASC