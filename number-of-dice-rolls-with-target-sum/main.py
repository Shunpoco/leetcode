class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        mod = 1000000007
        dp = [[0 for _ in range(target+1)] for _ in range(n)]
        
        for i in range(1, k+1):
            if i > target:
                break
            dp[0][i] = 1
            
        for i in range(1, n):
            s = 0
            right = 0
            left = right - k
            for j in range(1, target+1):
                s += dp[i-1][right]
                s %= mod
                if left >= 0:
                    s -= dp[i-1][left]
                    s %= mod
                right += 1
                left += 1

                dp[i][j] = s
                
        return dp[n-1][target]
