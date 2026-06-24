#discount impact
CREATE VIEW discount_impact as
select 
round(discount,1) discount_level,
sum(sales) revenue,
sum(profit) profit
from orders
group by discount_level
order by discount_level