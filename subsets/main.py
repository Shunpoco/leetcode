class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        stack = [([], 0)]
        result = []
        
        while len(stack) > 0:
            v, left = stack.pop(-1)
            result.append(v)
            
            candidates = nums[left:]

            for i, num in enumerate(candidates):
                temp = v.copy()
                temp.append(num)
                stack.append((temp, left+i+1))
                
        return result
