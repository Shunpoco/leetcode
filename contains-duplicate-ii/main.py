from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mem = {}
        
        for i, num in enumerate(nums):
            if mem.get(num) is not None:
                v = mem[num]
                if i - v <= k:
                    return True
                
            mem[num] = i
            
        return False

