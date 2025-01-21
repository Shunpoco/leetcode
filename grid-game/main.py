class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        f_sum = sum(grid[0])
        s_sum = 0

        min_sum = float("inf")

        for i in range(len(grid[0])):
            f_sum -= grid[0][i]

            min_sum = min(min_sum, max(f_sum, s_sum))
            s_sum += grid[1][i]

        return min_sum

