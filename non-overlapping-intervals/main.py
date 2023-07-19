from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda x: x[1])

        right = intervals[0][1]
        result = 0

        for i in range(1, len(intervals)):
            c = intervals[i]

            if c[0] < right:
                result += 1
            else:
                right = c[1]

        return result

