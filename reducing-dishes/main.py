from typing import List

class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        result = 0

        satisfaction.sort()

        s = sum(satisfaction)
        sums = sum([(i+1)*val for i, val in enumerate(satisfaction)])
        if sums > result:
            result = sums

        for v in satisfaction:
            sums -= s
            s -= v
            if sums > result:
                result = sums

        return result

