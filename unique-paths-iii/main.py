from typing import List, Tuple

class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        visited = [[0 for _ in range(m)] for _ in range(n)]
        start = (0, 0)
        end = (0, 0)
        for row in range(n):
            for col in range(m):
                v = grid[row][col]
                if v == 1:
                    start = (row, col)
                    visited[row][col] = 1
                elif v == 2:
                    end = (row, col)
                elif v == -1:
                    visited[row][col] = 1

        result = self.backtrack(start, end, visited, n, m)

        return result

    def backtrack(self, pos: Tuple[int, int], end: Tuple[int, int], visited: List[List[int]], n: int, m: int) -> int:
        if pos == end:
            if self.sums(visited) == n*m:
                return 1
            return 0

        result = 0
        row = pos[0]
        col = pos[1]
        if row-1 >= 0 and visited[row-1][col] == 0:
            visited[row-1][col] = 1
            result += self.backtrack((row-1, col), end, visited, n, m)
            visited[row-1][col] = 0
        if row+1 < n and visited[row+1][col] == 0:
            visited[row+1][col] = 1
            result += self.backtrack((row+1, col), end, visited, n, m)
            visited[row+1][col] = 0
        if col-1 >= 0 and visited[row][col-1] == 0:
            visited[row][col-1] = 1
            result += self.backtrack((row, col-1), end, visited, n, m)
            visited[row][col-1] = 0
        if col+1 < m and visited[row][col+1] == 0:
            visited[row][col+1] = 1
            result += self.backtrack((row, col+1), end, visited, n, m)
            visited[row][col+1] = 0

        return result

    def sums(self, visited: List[List[int]]):
        r = 0
        for visits in visited:
            r += sum(visits)

        return r
