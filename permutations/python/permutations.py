from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        stack = [([], 0)]
        result = []
        L = len(nums)
        while stack:
            perms, level = stack.pop(-1)
            for num in nums:
                if num not in perms:
                    temp = perms.copy()
                    temp.append(num)
                    if level+1 == L:
                        result.append(temp)
                    else:
                        stack.append((temp, level+1))
                        
        return result
        