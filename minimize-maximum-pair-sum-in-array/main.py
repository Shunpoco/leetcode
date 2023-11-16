from typing import List

class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()

        result = 0

        left, right = 0, len(nums)-1

        while left < right:
            v = nums[left] + nums[right]
            if v > result:
                result = v
            left += 1
            right -= 1

        return result

