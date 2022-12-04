from typing import List

class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        n = len(nums)
        
        cum = []
        t = 0
        for num in nums:
            t += num
            cum.append(t)
            
        min_diff = -1
        min_idx = -1
        
        for i in range(n):
            v1 = cum[i] // (i+1)
            v2 = (cum[-1]-cum[i]) // (n-i-1) if n-i-1 > 0 else 0
            
            diff = v1-v2 if v1 >= v2 else v2-v1
            
            if min_diff == -1 or min_diff > diff:
                min_diff = diff
                min_idx = i
                
        return min_idx
