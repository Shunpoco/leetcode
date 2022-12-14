from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [-1 for _ in range(len(nums))]
        
        return self.solve(nums, 0, dp)


    def solve(self, nums: List[int], idx: int, dp: List[int]) -> int:
        if idx >= len(nums):
            return 0

        if dp[idx] >= 0:
            return dp[idx]

        r = nums[idx] + self.solve(nums, idx+2, dp)
        if idx < len(nums)-1:
            r = max(r, nums[idx+1] + self.solve(nums, idx+3, dp))
        dp[idx] = r

        return r
