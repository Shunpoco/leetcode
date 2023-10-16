from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        a = [0, 1, 0]

        for _ in range(rowIndex):
            t = [0 for _ in range(len(a)+1)]
            for i in range(1, len(a)):
                t[i] = a[i]+a[i-1]

            a = t.copy()

        return a[1:len(a)-1]

