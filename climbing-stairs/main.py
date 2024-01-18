class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0 for _ in range(n+1)]
        dp[0] = 1

        return self.climb(n, dp)

    def climb(self, n: int, dp: List[int]) -> int:
        print(n)
        if n < 0:
            return 0

        if dp[n] > 0:
            return dp[n]

        r = self.climb(n-1, dp) + self.climb(n-2, dp)

        dp[n] = r

        return r
