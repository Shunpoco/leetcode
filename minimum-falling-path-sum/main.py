from typing import List

class Solution:
    MAX = 100000000000
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        nrow = len(matrix)
        ncol = len(matrix[0])
        memory = [[self.MAX for _ in range(ncol)] for _ in range(nrow)]

        result = self.MAX
        for row in range(nrow):
            t = self.solve(matrix, 0, row, nrow, ncol, memory)
            if result > t:
                result = t
        return result

    def solve(self, matrix: List[List[int]], row: int, col: int, nrow: int, ncol: int, memory: List[List[int]]) -> int:
        if row == nrow:
            return 0

        if memory[row][col] != self.MAX:
            return memory[row][col]
        
        t = self.solve(matrix, row+1, col, nrow, ncol, memory)

        if col-1 >= 0:
            t_ = self.solve(matrix, row+1, col-1, nrow, ncol, memory)
            if t_ < t:
                t = t_
        if col+1 < ncol:
            t_ = self.solve(matrix, row+1, col+1, nrow, ncol, memory)
            if t_ < t:
                t = t_

        r = matrix[row][col] + t
        memory[row][col] = r

        return r
