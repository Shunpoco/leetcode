class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        result = 0
        min_abs = float('inf')
        negatives = 0

        for r in matrix:
            for v in r:
                result += abs(v)
                if v < 0:
                    negatives += 1
                min_abs = min(min_abs, abs(v))

        if negatives % 2 != 0:
            result -= 2 * min_abs

        return result
