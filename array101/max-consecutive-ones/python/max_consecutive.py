from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        r = 0
        t = 0
        for num in nums:
            if num == 1:
                t += 1
                if t > r:
                    r = t
            else:
                t = 0
                
        return r
