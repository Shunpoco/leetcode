from typing import List

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxs = [-1] * len(arr)

        m = arr[len(arr)-1]
        for i in range(1, len(arr)):
            v = arr[len(arr)-i]
            m = max([m, v])
            if m > maxs[len(maxs)-1-i]:
                maxs[len(maxs)-1-i] = m
        return maxs