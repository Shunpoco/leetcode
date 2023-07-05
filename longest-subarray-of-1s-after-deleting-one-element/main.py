from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        ones = []

        t = 0
        for num in nums:
            if num == 1:
                t += 1
            else:
                ones.append(t)
                t = 0
        if t > 0:
            ones.append(t)

        n = len(ones)
        result = 0
        if n == 0:
            return result
        elif n == 1:
            return ones[0]-1

        for i in range(n-1):
            v = ones[i] + ones[i+1]
            if v > result:
                result = v

        return result

