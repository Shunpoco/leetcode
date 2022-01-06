class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        
        if len(nums) < 4:
            return result
        
        nums.sort()
        
        for i, num in enumerate(nums):
            if i == 0 or num != nums[i-1]:
                result.extend(self.threeSum(nums[i+1:], target-num, target))
            
        return result
    
    def threeSum(self, nums: List[int], target: int, origin: int) -> List[List[int]]:
        result = []
        
        for i, num in enumerate(nums):
            if i == 0 or num != nums[i-1]:
                temp = self.twoSum(nums[i+1:], target-num, target)
                for t in temp:
                    t.append(origin-target)
                    result.append(t)
                    
        return result
        
    
    
    def twoSum(self, nums: List[int], target: int, origin: int) -> List[List[int]]:
        result = []
        h = {}
        
        for i, num in enumerate(nums):
            if h.get(num) is not None:
                result.append([origin-target, h.get(num), num])
                del h[num]
                
            if i == 0 or num != nums[i-1]:
                h[target-num] = num
                
        return result

