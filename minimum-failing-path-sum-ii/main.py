class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        result = float('inf')

        dp = [[-1 for _ in range(n)] for _ in range(n)]

        for i in range(n):
            dp[0][i] = grid[0][i]

        for i in range(1, n):
            for j in range(n):
                t = float('inf')

                for k in range(n):
                    if j != k:
                        t = min(t, grid[i][j]+dp[i-1][k])

                dp[i][j] = t

        for j in range(n):
            result = min(result, dp[n-1][j])

        return result

