from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum = -1
        maximum = -1

        result = 0
        for price in prices:
            if minimum == -1 or minimum > price:
                minimum = price
                maximum = -1
            else:
                if price > minimum and price > maximum:
                    maximum = price

            result = max(result, maximum - minimum)

        return result
