#profitability check
select 
sum(sales),
sum(profit),
sum(profit)/sum(sales) margin
from orders