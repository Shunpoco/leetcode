class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zero_cells = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    zero_cells.append((i, j))

        while len(zero_cells) > 0:
            v = zero_cells.pop()

            # Entire the row
            for j in range(len(matrix[0])):
                matrix[v[0]][j] = 0

            # Entire the column
            for i in range(len(matrix)):
                matrix[i][v[1]] = 0

