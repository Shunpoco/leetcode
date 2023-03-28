from typing import List

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        nd = len(days)
        memo = [-1 for _ in range(nd)]

        def exec(idx: int) -> int:
            if idx >= nd:
                return 0

            if memo[idx] != -1:
                return memo[idx]
            
            v1 = costs[0] + exec(idx+1)
            v2 = costs[1]
            d = 0
            while idx+d < nd and days[idx+d] < days[idx] + 7:
                d += 1
            v2 += exec(idx+d)

            v3 = costs[2]
            d = 0
            while idx+d < nd and days[idx+d] < days[idx] + 30:
                d += 1
            v3 += exec(idx+d)

            v = min(v1, v2, v3)
            memo[idx] = v

            return v

        return exec(0)

