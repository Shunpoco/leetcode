from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        rows = [1]

        for _ in range(rowIndex):
            rows = self._row(rows)

        return rows

    def _row(self, before: List[int]) -> List[int]:
        r = []

        for i in range(len(before)):
            if i == 0:
                r.append(before[i])
            else:
                r.append(before[i-1] + before[i])

        r.append(before[i])

        return r
