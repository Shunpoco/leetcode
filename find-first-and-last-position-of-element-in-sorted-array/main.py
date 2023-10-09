class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]
        
        result = self.search(nums, target, 0)
        
        if not result:
            return [-1, -1]
        
        return [min(result), max(result)]
    
    
    def search(self, nums: List[int], target: int, start: int) -> List[int]:
        if len(nums) == 0:
            return []
        
        result = []
        medIdx = len(nums) // 2
        median = nums[medIdx]
        
        if target == median:
            result.append(medIdx+start)
            result.extend(self.search(nums[:medIdx], target, start))
            result.extend(self.search(nums[medIdx+1:], target, start+medIdx+1))
            
        elif target < median:
            result.extend(self.search(nums[:medIdx], target, start))
            
        else:
            result.extend(self.search(nums[medIdx+1:], target, start+medIdx+1))
            
        return result
