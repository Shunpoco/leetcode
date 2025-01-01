class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        memo = [-1 for _ in range(days[-1]+1)]
        needs = {}
        for day in days:
            needs[day] = True

        return self.dp(memo, needs, 1, days, costs)

    def dp(self, memo, needs, cur, days, costs):
        if cur > days[-1]:
            return 0

        if needs.get(cur) is None:
            return self.dp(memo, needs, cur+1, days, costs)

        if memo[cur] != -1:
            return memo[cur]

        od = costs[0] + self.dp(memo, needs, cur+1, days, costs)
        sd = costs[1] + self.dp(memo, needs, cur+7, days, costs)
        md = costs[2] + self.dp(memo, needs, cur+30, days, costs)

        memo[cur] = min([od, sd, md])

        return memo[cur]

