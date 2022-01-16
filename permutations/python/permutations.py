from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        stack = [([], 0)]
        result = []
        L = len(nums)
        
        while stack:
            p, l = stack.pop(-1)
            
            for num in nums:
                if num not in p:
                    t = p.copy()
                    t.append(num)
                    
                    if len(t) == L:
                        result.append(t)
                    else:
                        stack.append([t, l+1])
                        
        return result
