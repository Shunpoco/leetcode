# Write your MySQL query statement below
select
    name as `employee`
from (
    select
        a.name,
        a.salary,
        b.salary as manager_salary
    from employee as a
    inner join employee as b
    on a.managerid = b.id
) as c
where salary > manager_salary
