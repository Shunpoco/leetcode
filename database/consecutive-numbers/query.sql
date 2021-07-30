select
    distinct num as consecutivenums
from (
    select
        num,
        lead(num, 1) over(rows between unbounded preceding and unbounded following) as lead1,
        lead(num, 2) over(rows between unbounded preceding and unbounded following) as lead2
    from logs
) as hoge
where num = lead1 and num = lead2
