from typing import List

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        l = len(arr)
        i = 0
        while i < l-1:
            if arr[i] == 0:
                if i+2 < l:
                    arr[i+2:l] = arr[i+1:l-1]
                arr[i+1] = 0
                i += 2
            else:
                i += 1
