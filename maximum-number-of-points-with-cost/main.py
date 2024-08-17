class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n, m = len(points), len(points[0])
        prev = points[0]

        for r in range(1, n):
            lm = [0 for _ in range(m)]
            rm = [0 for _ in range(m)]
            cur = [0 for _ in range(m)]

            lm[0] = prev[0]
            for c in range(1, m):
                lm[c] = max(lm[c-1]-1, prev[c])

            rm[-1] = prev[-1]
            for c in range(m-2, -1, -1):
                rm[c] = max(rm[c+1]-1, prev[c])

            for c in range(m):
                cur[c] = points[r][c] + max(lm[c], rm[c])

            prev = cur

        return max(prev)
