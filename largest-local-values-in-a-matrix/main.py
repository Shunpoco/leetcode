class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        p = []

        for i in range(n):
            t = []
            for j in range(1, n-1):
                t.append(max(grid[i][j-1], grid[i][j], grid[i][j+1]))
            p.append(t)

        r = []
        for i in range(1, n-1):
            t = []
            for j in range(len(p[i])):
                t.append(max(p[i-1][j], p[i][j], p[i+1][j]))

            r.append(t)

        return r

