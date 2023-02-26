from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        min_ = prices[0]

        r = 0
        for i in range(1, n):
            min_ = min(prices[i], min_)
            r = max(prices[i]-min_, r)

        return r
             
