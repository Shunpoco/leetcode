from typing import List

class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()

        cums = [0 for _ in range(len(nums)+1)]
        v = 0
        for i in range(len(nums)):
            v += nums[i]
            cums[i+1] = v

        result = 0
        left = 0
        for i in range(len(nums)):
            while nums[i] * (i-left+1) - (cums[i+1]-cums[left]) > k:
                left += 1

            result = max(result, i-left+1)

        return result

