from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # return self._calculate(prices, 0)
        return self._calc(prices)
    # Using differences
    def _calc(self, prices: List[int]) -> int:
        res = 0
        for i in range(len(prices)-1):
            diff = prices[i+1] - prices[i]
            if diff > 0:
                res += diff

        return res


    # Brute force, maybe time exceeded
    def _calculate(self, prices: List[int], s: int) -> int:
        l = len(prices)
        if s >= l:
            return 0
        m = 0

        for i in range(s, l):
            mProfit = 0
            for j in range(i+1, l):
                if (prices[i] < prices[j]):
                    profit = prices[j] - prices[i] + self._calculate(prices, j+1)

                    if (profit > mProfit):
                        mProfit = profit

            if (mProfit > m):
                m = mProfit

        return m
