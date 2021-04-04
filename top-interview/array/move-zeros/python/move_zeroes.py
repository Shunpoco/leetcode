from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i = 0
        c = 0
        for _ in range(len(nums)):
            if nums[i] == 0:
                v = nums.pop(i)
                c += 1
                continue
            i += 1
        nums.extend([0]*c)
