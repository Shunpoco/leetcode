class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        dp = [-1] * n

        return self.solve(0, nums, dp)

    def solve(self, i: int, nums: List[int], dp: List[int]) -> 0:
        if i >= len(nums):
            return 0

        if dp[i] >= 0:
            return dp[i]


        r = nums[i] + self.solve(i+2, nums, dp)
        r2 = self.solve(i+1, nums, dp)

        if r2 > r:
            r = r2

        dp[i] = r

        return r

