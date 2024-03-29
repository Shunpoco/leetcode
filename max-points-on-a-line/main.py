from typing import List

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) == 1:
            return 1
        points.sort()
        result = 2
        for i in range(len(points)-1):
            for j in range(len(points)-1, i+1, -1):
                if j-i+1 <= result:
                    break
                v = self.contains(i, j, points)
                if v > result:
                    result = v

        return result

    def contains(self, i: int, j: int, points: List[List[int]]) -> int:
        p1 = points[i]
        p2 = points[j]
        r = 2
        y2my1 = p2[1] - p1[1]
        x2mx1 = p2[0] - p1[0]
        b = p1[1] * x2mx1 - y2my1 * p1[0]
        for k in range(i+1, j):
            v = points[k]
            if v[1] * x2mx1 == v[0] * y2my1 + b:
                r += 1

        return r
