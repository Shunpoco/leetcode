from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        m = max(candies)

        result = [False for _ in range(len(candies))]

        for i, v in enumerate(candies):
            if v + extraCandies >= m:
                result[i] = True

        return result

