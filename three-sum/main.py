from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        if len(nums) < 3:
            return result
        
        nums.sort()
        
        for i, num in enumerate(nums):
            if num > 0:
                break
                
            if i == 0 or num != nums[i-1]:
                result.extend(self.twoSum(nums[i+1:], -num))
        
        return result
    
    def twoSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        h = {}
        
        for i, num in enumerate(nums):
            if h.get(num) is not None:
                result.append([-target, h.get(num), num])
                del h[num]
            
            if i == 0 or num != nums[i-1]:
                h[target-num] = num
        
        return result
