from typing import List

class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        result = 0
        
        start = points.pop(0)

        for point in points:
            dx, dy = abs(point[0]-start[0]), abs(point[1]-start[1])

            while dx > 0 or dy > 0:
                if dx > 0 and dy > 0:
                    dx -= 1
                    dy -= 1
                elif dx > 0:
                    dx -= 1
                elif dy > 0:
                    dy -= 1

                result += 1

            start = point

        return result
