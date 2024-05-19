class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        n = len(nums)

        dp = [[0, 0] for _ in range(n+1)]
        dp[n][1] = 0
        dp[n][0] = -float('inf')

        for i in range(n-1, -1, -1):
            for even in range(2):
                po = dp[i+1][even^1] + (nums[i]^k)
                dpo = dp[i+1][even] + nums[i]

                dp[i][even] = max(po, dpo)

        return dp[0][1]
