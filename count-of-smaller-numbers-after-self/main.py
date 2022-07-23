from typing import List

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)
        enumerates = list(enumerate(nums)) # [[0, 5], [1, 2], [2, 6], [3, 1]]
        
        def sort(enumerates: List[List[int]]) -> List[List[int]]:
            mid = len(enumerates) // 2
            
            if mid > 0:
                left, right = sort(enumerates[:mid]), sort(enumerates[mid:])
                for i in range(len(enumerates))[::-1]:
                    if not right or left and left[-1][1] > right[-1][1]:
                        result[left[-1][0]] += len(right)
                        enumerates[i] = left.pop()
                    else:
                        enumerates[i] = right.pop()
            
            return enumerates
        
        sort(enumerates)
        
        return result
                
