from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        visited = [[False for _ in range(n+2)] for _ in range(m+2)]
        for i in range(m+2):
            for j in range(n+2):
                if i == 0 or i == m+1 or j == 0 or j == n+1:
                    visited[i][j] = True

        result = []

        self.exec(0, 0, 'r', matrix, result, m, n, visited)

        return result

    def exec(self, row: int, col: int, direction: str, matrix: List[List[int]], result: List[int], m: int, n: int, visited: List[List[bool]]):
        result.append(matrix[row][col])
        r, c = row+1, col+1
        visited[r][c] = True

        if direction == 'r':
            # right to bottom
            if visited[r][c+1] and not visited[r+1][c]:
                self.exec(row+1, col, 'b', matrix, result, m, n, visited)
            elif not visited[r][c+1]:
                self.exec(row, col+1, 'r', matrix, result, m, n, visited)

        elif direction == 'b':
            # bottom to left
            if visited[r+1][c] and not visited[r][c-1]:
                self.exec(row, col-1, 'l', matrix, result, m, n, visited)
            elif not visited[r+1][c]:
                self.exec(row+1, col, 'b', matrix, result, m, n, visited)

        elif direction == 'l':
            # left to top
            if visited[r][c-1] and not visited[r-1][c]:
                self.exec(row-1, col, 't', matrix, result, m, n, visited)
            elif not visited[r][c-1]:
                self.exec(row, col-1, 'l', matrix, result, m, n, visited)

        elif direction == 't':
            # top to right
            if visited[r-1][c] and not visited[r][c+1]:
                self.exec(row, col+1, 'r', matrix, result, m, n, visited)
            elif not visited[r-1][c]:
                self.exec(row-1, col, 't', matrix, result, m, n, visited)
