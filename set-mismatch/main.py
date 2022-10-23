from typing import List

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        r = [0]*n
        
        dup = -1
        for num in nums:
            r[num-1] += 1
            if r[num-1] == 2:
                dup = num
                
        no = -1
        for i, v in enumerate(r):
            if v == 0:
               no = i+1
            
        return [dup, no]
