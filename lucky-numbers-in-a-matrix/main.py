class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        mrow, mcol = [float('inf') for _ in range(len(matrix))], [-float('inf') for _ in range(len(matrix[0]))]

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                v = matrix[i][j]
                if v < mrow[i]:
                    mrow[i] = v
                if v > mcol[j]:
                    mcol[j] = v

        result = []

        for r in mrow:
            if r in mcol:
                result.append(r)

        return result
