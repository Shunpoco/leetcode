from typing import List

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()

        result = 0
        while len(piles) > 0:
            piles.pop(-1)
            result += piles.pop(-1)
            piles.pop(0)

        return result
