from typing import List

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()

        result = 0
        idx = 0
        while coins > 0 and idx < len(costs) and coins >= costs[idx]:
            result += 1
            coins -= costs[idx]
            idx += 1

        return result
