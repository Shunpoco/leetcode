from typing import List

class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        diff = [d // s if d % s == 0 else d // s + 1 for d, s in zip(dist, speed)]

        diff.sort()

        minute = 0
        idx = 0

        while idx < len(diff):
            if diff[idx] - minute > 0:
                idx += 1
            else:
                return idx

            minute += 1

        return idx

