#sales by category
select 
p.category,
sum(o.sales)
from orders o
join products p 
ON o.product_id = p.product_id
group by p.category