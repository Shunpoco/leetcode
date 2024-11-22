class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        cols = len(matrix[0])
        result = 0

        for row in matrix:
            flipped = [1-x for x in row]

            count = sum(1 for r in matrix if r == row or r == flipped)

            result = max(result, count)

        return result
