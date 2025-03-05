class Solution:
    def coloredCells(self, n: int) -> int:
        result = 1

        for i in range(2, n+1):
            result += (i-1)*4

        return result

