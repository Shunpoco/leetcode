from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        cumulatives = []
        t = 0
        for num in nums:
            t += num
            cumulatives.append(t)

        return cumulatives

