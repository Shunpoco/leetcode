from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        cumulatives = [0 for _ in range(len(nums))]
        t = 0
        for i, num in enumerate(nums):
            t += num
            cumulatives[i] = t

        return cumulatives
