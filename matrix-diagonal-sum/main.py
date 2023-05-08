class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        result = 0

        for i in range(n):
            x1 = i
            y1 = i
            x2 = n-1-i
            y2 = i
            result += mat[x1][y1]
            if x1 != x2:
                result += mat[x2][y2]

        return result
