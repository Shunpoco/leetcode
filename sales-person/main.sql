# Write your MySQL query statement below
select
    distinct name
from (

select
    name,
    order_id
from salesperson a
left outer join (
select
    order_id,
    sales_id
from orders
inner join (
    select
        com_id
    from company
    where name = "RED"
) c
on orders.com_id = c.com_id
) b
on a.sales_id = b.sales_id
    ) d
where order_id is null
