# Write your MySQL query statement below
select
    email
from (
    select
        email,
        count(1) as c
    from person
    group by email
) as p
where c > 1
