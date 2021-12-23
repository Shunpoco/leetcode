class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        
        result = []
        
        for i, num in enumerate(nums):
            if num > 0:
                break
            if i > 0 and num == nums[i-1]:
                continue
            result.extend(self.twoSum(nums[i+1:], -nums[i]))
            
        return result
    
    def twoSum(self, nums: List[int], target: int) -> List[List[int]]:
        memory = {}
        result = []
        for i, num in enumerate(nums):
            if memory.get(num) is not None:
                result.append([-target, memory[num], num])
                del memory[num]
            elif i == 0 or num != nums[i-1]:
                memory[target-num] = num
                
        return result
