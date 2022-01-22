class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        stack = [[]]
        
        nums = list(range(1, n+1))
        result = []
        
        while len(stack) > 0:
            vals = stack.pop(-1)
            
            if len(vals) > 0:
                nums_temp = nums[vals[-1]:]
            else:
                nums_temp = nums

            for num in nums_temp:
                if num not in vals:
                    temp = vals.copy()
                    temp.append(num)
                    
                    if len(temp) == k:
                        result.append(temp)
                    else:
                        stack.append(temp)
                        
        return result

