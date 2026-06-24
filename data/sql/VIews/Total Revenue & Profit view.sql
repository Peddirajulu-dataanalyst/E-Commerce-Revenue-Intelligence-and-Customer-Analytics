#Total Revenue & Profit (Main KPI)
CREATE VIEW total_revenue_profit as 
select 
sum(sales) as total_revenue,
sum(profit) as total_profit,
sum(profit)/sum(sales) as profit_margin
from orders