from typing import List

class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        count = 0
        prev = -1
        for a in arr:
            if a != prev:
                count = 1
                prev = a
            else:
                count += 1

            if 4*count > n:
                return a

        return -1
