from typing import List

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        result = [[0 for _ in range(n)] for _ in range(n)]

        self.exec(0, 0, 1, result, 'r', n)

        return result

    def exec(self, row: int, col: int, val: int, result: List[List[int]], d: str, n: int):
        if result[row][col] > 0:
            return

        result[row][col] = val

        if d == 'r':
            if col+1 == n or result[row][col+1] > 0:
                if row+1 < n:
                    self.exec(row+1, col, val+1, result, 'b', n)
            else:
                self.exec(row, col+1, val+1, result, 'r', n)

        elif d == 'b':
            if row+1 == n or result[row+1][col] > 0:
                if col-1 >= 0:
                    self.exec(row, col-1, val+1, result, 'l', n)
            else:
                self.exec(row+1, col, val+1, result, 'b', n)

        elif d == 'l':
            if col-1 == -1 or result[row][col-1] > 0:
                if row-1 >= 0:
                    self.exec(row-1, col, val+1, result, 't', n)
            else:
                self.exec(row, col-1, val+1, result, 'l', n)

        elif d == 't':
            if row-1 == -1 or result[row-1][col] > 0:
                if col+1 < n:
                    self.exec(row, col+1, val+1, result, 'r', n)
            else:    
                self.exec(row-1, col, val+1, result, 't', n)

