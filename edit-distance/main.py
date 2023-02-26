class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]

        for i in range(m+1):
            for j in range(n+1):
                if i == 0 and j == 0:
                    continue
                if i == 0:
                    dp[i][j] = dp[i][j-1] + 1
                elif j == 0:
                    dp[i][j] = dp[i-1][j] + 1
                else:
                    if word1[j-1] == word2[i-1]:
                        dp[i][j] = min(dp[i-1][j-1], dp[i-1][j]+1, dp[i][j-1]+1)
                    else:
                        dp[i][j] = min(dp[i-1][j-1]+1, dp[i-1][j]+1, dp[i][j-1]+1)

        return dp[m][n]

