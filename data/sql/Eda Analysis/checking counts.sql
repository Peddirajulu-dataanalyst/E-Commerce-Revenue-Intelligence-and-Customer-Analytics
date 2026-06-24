#checking counnts of records
select count(*) from orders;
select count(DISTINCT customer_id) from orders;
select count(DISTINCT product_id) from orders;
select MIN(order_date),MAX(order_date) from orders;