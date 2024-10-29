class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        memo = [[-1 for _ in range(n)] for _ in range(m)]

        result = 0
        for i in range(m):
            self.calc(i, 0, grid, memo)
            if memo[i][0] > result:
                result = memo[i][0]

        return result

    def calc(self, i, j, grid, memo):
        if memo[i][j] >= 0:
            return

        result = 0

        if i - 1 >= 0 and j + 1 < len(grid[0]) and grid[i][j] < grid[i-1][j+1]:
            self.calc(i-1, j+1, grid, memo)
            t = 1 + memo[i-1][j+1]
            if t > result:
                result = t

        if j + 1 < len(grid[0]) and grid[i][j] < grid[i][j+1]:
            self.calc(i, j+1, grid, memo)
            t = 1 + memo[i][j+1]
            if t > result:
                result = t

        if i + 1 < len(grid) and j + 1 < len(grid[0]) and grid[i][j] < grid[i+1][j+1]:
            self.calc(i+1, j+1, grid, memo)
            t = 1 + memo[i+1][j+1]
            if t > result:
                result = t

        memo[i][j] = result
