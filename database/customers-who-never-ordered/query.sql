# Write your MySQL query statement below
select
    name as customers
from customers
left outer join orders
on customers.id = orders.customerid
where customerid is null
