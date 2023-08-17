from typing import List

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])

        result = [[-1 for _ in range(n)] for _ in range(m)]

        q = []

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    result[i][j] = 0
                    q.append((i, j, 0))

        while len(q) > 0:
            row, col, dist = q.pop(0)

            if row > 0 and (result[row-1][col] == -1 or result[row-1][col] > dist+1):
                result[row-1][col] = dist+1
                q.append((row-1, col, dist+1))

            if row < m-1 and (result[row+1][col] == -1 or result[row+1][col] > dist+1):
                result[row+1][col] = dist+1
                q.append((row+1, col, dist+1))

            if col > 0 and (result[row][col-1] == -1 or result[row][col-1] > dist+1):
                result[row][col-1] = dist+1
                q.append((row, col-1, dist+1))

            if col < n-1 and (result[row][col+1] == -1 or result[row][col+1] > dist+1):
                result[row][col+1] = dist+1
                q.append((row, col+1, dist+1))

        return result

