# Write your MySQL query statement below
select
    a.id,
    case
        when a.le is null and a.id % 2 = 1 then a.student
        when a.id % 2 = 1 then b.student
        else c.student
    end as student
from (
    select
        id,
        student,
        lead(id) over(order by id) as le,
        lag(id) over(order by id) as la
    from
        seat
) a
left join seat b
on a.le = b.id
left join seat c
on a.la = c.id
