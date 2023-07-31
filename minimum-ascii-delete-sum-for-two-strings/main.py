class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        n, m = len(s1), len(s2)
        dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

        for i in range(n+1):
            for j in range(m+1):
                if i == 0 and j == 0:
                    dp[i][j] = 0
                elif i == 0:
                    dp[i][j] = dp[i][j-1] + ord(s2[j-1])
                elif j == 0:
                    dp[i][j] = dp[i-1][j] + ord(s1[i-1])
                else:
                    if s1[i-1] == s2[j-1]:
                        dp[i][j] = dp[i-1][j-1]
                    else:
                        dp[i][j] = min(
                            dp[i][j-1] + ord(s2[j-1]),
                            dp[i-1][j] + ord(s1[i-1]),
#                            dp[i-1][j-1] + ord(s2[j-1]) + ord(s1[i-1]),
                        )

        return dp[n][m]

