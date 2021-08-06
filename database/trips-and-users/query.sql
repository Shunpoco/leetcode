# Write your MySQL query statement below
select
    request_at as day,
    round(sum(case when status = 'completed' then 0 else 1 end) / sum(1), 2)  as `cancellation rate`
from (
    select
        request_at,
        a.banned as client_banned,
        b.banned as driver_banned,
        status
    from trips
    left join users as a
    on trips.client_id = a.users_id
    left join users as b
    on trips.driver_id = b.users_id
) d
where 
    client_banned = 'No' and driver_banned = 'No'
    and request_at between date('2013-10-01') and date('2013-10-03')
group by request_at
