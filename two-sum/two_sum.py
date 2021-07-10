from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        
        for idx in range(len(nums)):
            v = nums[idx]
            h[target-v] = idx
            
        for idx in range(len(nums)):
            v = nums[idx]
            
            if h.get(v) and h[v] != idx:
                return [idx, h[v]]
                        
        return []
