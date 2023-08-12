from typing import List, Tuple, Dict

class Solution:
    def uniquePathsWithObstacles(self, og: List[List[int]]) -> int:
        m, n = len(og), len(og[0])

        memo = [[-1 for _ in range(n)] for _ in range(m)]

        self.calc(0, 0, og, memo)

        return memo[0][0]

    def calc(self, row: int, col: int, og: List[List[int]], memo: List[List[int]]):
        if memo[row][col] >= 0:
            return

        if og[row][col] == 1:
            memo[row][col] = 0
            return

        if row == len(og)-1 and col == len(og[0]) - 1:
            memo[row][col] = 1
            return

        r = 0

        if row < len(og)-1:
            self.calc(row+1, col, og, memo)
            r += memo[row+1][col]

        if col < len(og[0])-1:
            self.calc(row, col+1, og, memo)
            r += memo[row][col+1]

        memo[row][col] = r
