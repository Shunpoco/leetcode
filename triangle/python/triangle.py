from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        l = len(triangle)
        for level in range(l-2, -1, -1):
            for idx in range(len(triangle[level])):
                triangle[level][idx] += min(
                    triangle[level+1][idx],
                    triangle[level+1][idx+1],
                )

        return triangle[0][0]
