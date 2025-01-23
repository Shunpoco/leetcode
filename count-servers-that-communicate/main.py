class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        row_counter = [0] * len(grid[0])
        col_counter = [0] * len(grid)

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    row_counter[col] += 1
                    col_counter[row] += 1

        result = 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    if row_counter[col] > 1 or col_counter[row] > 1:
                        result += 1

        return result

