from typing import List

class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        m = max(arr)

        if k >= len(arr):
            return m

        mi = arr.index(m)

        v = arr[0]
        c = 0

        for i in range(1, mi+1):
            if v > arr[i]:
                c += 1
            else:
                v = arr[i]
                c = 1

            if c == k:
                return v

        return m

