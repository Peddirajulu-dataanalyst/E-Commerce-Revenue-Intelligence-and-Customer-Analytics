#sales by channel
select 
channel,
sum(sales)
from orders
group by channel
