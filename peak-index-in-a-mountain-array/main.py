from typing import List

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        return self.exec(0, len(arr), arr)

    def exec(self, left: int, right: int, arr: List[int]) -> int:
        if left == right:
            return left


        m = (left+right) // 2

        if m == 0 or m == len(arr)-1:
            return -1

        if arr[m-1] < arr[m] and arr[m] > arr[m+1]:
            return m

        elif arr[m] < arr[m+1]:
            return self.exec(m, right, arr)

        else:
            return self.exec(left, m, arr)
