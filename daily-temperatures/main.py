from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = []
        for idx, temperature in reversed(list(enumerate(temperatures))):
            while len(stack) > 0 and stack[-1][0] <= temperature:
                stack.pop()
            
            ans = 0 if len(stack) == 0 else stack[-1][1]-idx
            stack.append((temperature, idx))

            result.insert(0, ans)
            
        return result

