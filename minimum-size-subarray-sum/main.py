from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left, right = 0, 0
        result = 0
        t = nums[0]
        while left <= right and right < len(nums):
            if t >= target:
                if result == 0 or result > right-left+1:
                    result = right-left+1
                t -= nums[left]
                left += 1
            else:
                right += 1
                if right < len(nums):
                    t += nums[right]

        return result
