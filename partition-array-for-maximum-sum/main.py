class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        dp = [-1 for _ in range(len(arr)+1)]

        self.solve(0, arr, k, dp)

        return dp[0]

    def solve(self, idx, arr, k, dp):
        if dp[idx] != -1:
            return

        if idx == len(dp):
            dp[idx] = 0
            return

        m = -1
        r = 0
        for i in range(k):
            if idx+i >= len(arr):
                break
            m = max(m, arr[idx+i])
            self.solve(idx+i+1, arr, k, dp)
            t = (i+1) * m  + dp[idx+i+1]
            if t > r :
                r = t

        dp[idx] = r

        return
