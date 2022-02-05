from typing import List

# class Solution:
#     def permute(self, nums: List[int]) -> List[List[int]]:
#         stack = [([], 0)]
#         result = []
#         L = len(nums)
        
#         while stack:
#             p, l = stack.pop(-1)
            
#             for num in nums:
#                 if num not in p:
#                     t = p.copy()
#                     t.append(num)
                    
#                     if len(t) == L:
#                         result.append(t)
#                     else:
#                         stack.append([t, l+1])
                        
#         return result


# Using backtrack
from collections import Counter

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        c = Counter()
        
        for num in nums:
            c[num] += 1
            
        result = []

        self.backtrack(nums, [], result, c)
        
        return result

    def backtrack(self, nums: List[int], v: List[int], result: List[List[int]], c: Counter):
        if len(v) == len(nums):
            result.append(v.copy())
            return
        
        for num in nums:
            if c[num] -1 >= 0:
                v.append(num)
                c[num] -= 1
                self.backtrack(nums, v, result, c)
                c[num] += 1
                v.pop(-1)
