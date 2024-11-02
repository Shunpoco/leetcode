class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        result = 0

        dp = [[-1 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                result += self.calc(i, j, matrix, dp)

        return result

    def calc(self, i, j, grid, dp):
        if i >= len(grid) or j >= len(grid[0]):
            return 0

        if grid[i][j] == 0:
            return 0

        if dp[i][j] != -1:
            return dp[i][j]

        right = self.calc(i, j+1, grid, dp)
        diagonal = self.calc(i+1, j+1, grid, dp)
        below = self.calc(i+1, j, grid, dp)
        dp[i][j] = 1 + min(right, min(diagonal, below))

        return dp[i][j]
