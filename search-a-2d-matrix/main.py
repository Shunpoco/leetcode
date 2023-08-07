from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        row = self.searchRow(target, 0, m, matrix)

        return self.searchCol(target, 0, n, row, matrix)


    def searchRow(self, target: int, top: int, bottom: int, mat: List[List[int]]) -> int:
        if top >= bottom-1:
            return top

        m = (top + bottom) // 2

        if mat[m][0] == target:
            return m

        elif mat[m][0] > target:
            return self.searchRow(target, top, m, mat)

        else:
            return self.searchRow(target, m, bottom, mat)

    def searchCol(self, target: int, left: int, right: int, row: int, mat: List[List[int]]) -> bool:
        if left == right:
            return mat[row][left] == target if left < len(mat[0]) else False


        m = (left+right) // 2

        if mat[row][m] == target:
            return True

        elif mat[row][m] > target:
            return self.searchCol(target, left, m, row, mat)

        return self.searchCol(target, m+1, right, row, mat)
