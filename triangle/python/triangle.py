from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for level in range(len(triangle)-2, -1,-1):
            for idx in range(level+1):
                triangle[level][idx] += min(
                    triangle[level+1][idx],
                    triangle[level+1][idx+1],
                )

        return triangle[0][0]
