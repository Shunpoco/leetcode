from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        mins = [0 for _ in range(n)]

        r = 0
        for i in range(n):
            if i == 0:
                mins[i] = prices[i]
            else:
                mins[i] = min(prices[i], mins[i-1])
                v = prices[i] - mins[i-1]
                if v > r:
                    r = v

        return r
             
