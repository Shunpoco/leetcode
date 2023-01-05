from typing import List

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()

        result = 0
        start = points[0][0]
        end = points[0][1]

        for i in range(1, len(points)):
            p = points[i]
            if end < p[0]:
                result += 1
                start = p[0]
                end = p[1]
            else:
                start = p[0]
                if end > p[1]:
                    end = p[1]
        result += 1
        return result

