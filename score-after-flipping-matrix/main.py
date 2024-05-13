class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])

        result = (1 << (m-1)) * n

        for j in range(1, m):
            v = 1 << (m - 1 - j)
            count = 0

            for i in range(n):
                if grid[i][j] == grid[i][0]:
                    count += 1

            result += max(count, n - count) * v

        return result

