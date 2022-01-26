class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()        
        
        stack = [([], 0)]
        result = []
        
        while len(stack) > 0:
            vs, lv = stack.pop(-1)
            result.append(vs)
            cds = nums[lv:]
            
            for i, cd in enumerate(cds):
                if i == 0 or cd != cds[i-1]:
                    temp = vs.copy()
                    temp.append(cd)
                    stack.append((temp, lv+i+1))
                
        return result
