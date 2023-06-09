from typing import List

class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        diffs = [x - y for x, y in zip(capacity, rocks)]
        diffs.sort()

        result = 0
        for diff in diffs:
            if additionalRocks < diff:
                break
            result += 1
            additionalRocks -= diff

        return result
