class Solution:
    def knightDialer(self, n: int) -> int:
        mod = 10 ** 9 + 7
        memo = {
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [3, 9, 0],
            5: [],
            6: [1, 7, 0],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4],
            0: [4, 6],
        }

        dp = [[0 for _ in range(n+1)] for _ in range(10)]

        for i in range(1, n+1):
            for j in range(10):
                if i == 1:
                    dp[j][i] = 1
                else:
                    for num in memo[j]:
                        dp[j][i] += dp[num][i-1]
                        dp[j][i] %= mod

        result = 0
        for i in range(10):
            result += dp[i][n]
            result %= mod

        return result
