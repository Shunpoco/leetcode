class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        result = [[0 for _ in range(len(colSum))] for _ in range(len(rowSum))]

        for c in range(len(colSum)):
            for r in range(len(rowSum)):
                v = min(colSum[c], rowSum[r])
                colSum[c] -= v
                rowSum[r] -= v
                result[r][c] = v

        return result
