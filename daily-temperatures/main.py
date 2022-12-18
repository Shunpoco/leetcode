from typing import List

# https://leetcode.com/problems/daily-temperatures/solutions/109818/simple-python-solution-w-explanation/

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        memo = [-1 for _ in range(100-30+1)]
        result = [0 for _ in range(len(temperatures))]

        for idx, temperature in reversed(list(enumerate(temperatures))):
            t = [x for x in memo[temperature-30+1:] if x > -1]
            r = 0 if len(t) == 0 else min(t) - idx
            result[idx] = r
            memo[temperature-30] = idx

        return result
