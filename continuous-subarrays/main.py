class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        memo = {}
        l, r = 0, 0
        result = 0

        while r < len(nums):
            memo[nums[r]] = memo.get(nums[r], 0) + 1
            while max(memo) - min(memo) > 2:
                memo[nums[l]] -= 1
                if memo[nums[l]] == 0:
                    del memo[nums[l]]
                l += 1
            result += r - l + 1
            r += 1

        return result

