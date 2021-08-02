# Write your MySQL query statement below
select
    d.name as department,
    e.name as employee,
    salary
from (
    select
        departmentid,
        name,
        salary,
        rank() over(partition by departmentid order by salary desc) as r
    from employee
) as e
inner join department as d
on e.departmentid = d.id
where e.r = 1
