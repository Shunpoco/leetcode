# Write your MySQL query statement below
select
    id
from (
    select
        id,
        case when date_sub(recorddate, interval 1 day) = lag(recorddate) over(order by recorddate)
        then temperature - lag(temperature) over(order by recorddate)
        else -1 end as diff
    from weather
) d
where diff > 0
