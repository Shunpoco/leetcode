from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        r = 0
        c = -101
        
        for num in nums:            
            if num != c:
                c = num
                nums[r] = num
                r += 1
        
        return r
