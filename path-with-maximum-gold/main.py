class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        memo = [[False for _ in range(n)] for _ in range(m)]

        result = 0
        for i in range(m):
            for j in range(n):
                t = self.bt(i, j, grid, memo)
                if t > result:
                    result = t

        return result

    def bt(self, i, j, grid, memo):
        if grid[i][j] == 0:
            return 0

        t = grid[i][j]
        r = t
        memo[i][j] = True
        if j - 1 >= 0 and not memo[i][j-1]:
            v = self.bt(i, j-1, grid, memo)
            if t+v > r:
                r = t+v
        if j + 1 < len(grid[0]) and not memo[i][j+1]:
            v = self.bt(i, j+1, grid, memo)
            if t+v > r:
                r = t+v
        if i - 1 >= 0 and not memo[i-1][j]:
            v = self.bt(i-1, j, grid, memo)
            if t + v > r:
                r = t+v
        if i + 1 < len(grid) and not memo[i+1][j]:
            v = self.bt(i+1, j, grid, memo)
            if t+v > r:
                r = t+v

        memo[i][j] = False

        return r

