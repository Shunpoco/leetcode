from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [-1 for _ in range(n+2)]
        dp[n] = 0
        dp[n+1] = float("inf")

        for i in range(n-1, -1, -1):
            dp[i] = min(cost[i]+dp[i+1], cost[i]+dp[i+2])

        return min(dp[0], dp[1])
