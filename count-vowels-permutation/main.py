class Solution:
    def countVowelPermutation(self, n: int) -> int:
        mod = 1000000007

        dp = [[0 for _ in range(5)] for _ in range(n+1)]

        for i in range(n+1):
            for j in range(5):
                if i == 0:
                    dp[i][j] = 0
                elif i == 1:
                    dp[i][j] = 1
                else:
                    # a
                    if j == 0:
                        dp[i][j] = dp[i-1][1] + dp[i-1][2] + dp[i-1][4]
                    elif j == 1:
                        dp[i][j] = dp[i-1][0] + dp[i-1][2]
                    elif j == 2:
                        dp[i][j] = dp[i-1][1] + dp[i-1][3]
                    elif j == 3:
                        dp[i][j] = dp[i-1][2]
                    else:
                        dp[i][j] = dp[i-1][2] + dp[i-1][3]

                dp[i][j] %= mod

        result = 0
        for j in range(5):
            result += dp[n][j]
            result %= mod

        return result

