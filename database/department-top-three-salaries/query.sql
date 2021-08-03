# Write your MySQL query statement below
select
    d.name as `department`,
    e.name as `employee`,
    e.salary
from (
    select
        name,
        salary,
        departmentid,
        dense_rank() over(partition by departmentid order by salary desc) as r
    from employee
) e
inner join department d
on e.departmentid = d.id
where e.r <= 3
