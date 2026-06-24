#Missing values Check
select 
sum(customer_id IS NULL),
sum(product_id IS NULL),
sum(sales IS NULL),
sum(profit IS NULL)
from orders