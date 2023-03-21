from typing import List

class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        result = 0
        l = 0
        r = 0
        while l < len(nums) and r < len(nums):
            if nums[r] != 0:
                d = r - l
                result += (d+1)*d//2  

                l = r + 1
                r = l
            else:
                r += 1

        if r != l:
            d = r - l
            result += (d+1)*d//2

        return result

