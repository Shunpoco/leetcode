class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOD = 10 ** 9 + 7
        dp = [[[0 for _ in range(n)] for _ in range(m)] for _ in range(maxMove+1)]

        for i in range(1, maxMove+1):
            for j in range(m):
                for k in range(n):
                    t = 0

                    t += 1 if j == 0 else dp[i-1][j-1][k]
                    t %= MOD

                    t += 1 if j == m - 1 else dp[i-1][j+1][k]
                    t %= MOD

                    t += 1 if k == 0 else dp[i-1][j][k-1]
                    t %= MOD

                    t += 1 if k == n - 1 else dp[i-1][j][k+1]
                    t %= MOD

                    dp[i][j][k] = t

        return dp[maxMove][startRow][startColumn]
