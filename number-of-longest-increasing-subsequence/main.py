
from typing import List

class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        result = [(1,1) for _ in range(n)]

        for i in range(n-1, -1, -1):
            v, t = 1, 1
            for j in range(i+1, n):
                if nums[j] > nums[i]:
                    v_, t_ = result[j]
                    v_ += 1
                    if v_ > v:
                        v, t = v_, t_
                    elif v_ == v:
                        t += t_
            result[i] = (v, t)

        v, t = 0, 0
        for v_, t_ in result:
            if v_ > v:
                v = v_
                t = t_
            elif v_ == v:
                t += t_

        return t

