class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)

        for i in range(n):
            t = [grid[i+j][j] for j in range(n-i)]
            t.sort(reverse=True)
            for j in range(n-i):
                grid[i+j][j] = t[j]

        for j in range(1, n):
            t = [grid[i][j+i] for i in range(n-j)]
            t.sort()
            for i in range(n-j):
                grid[i][j+i] = t[i]

        return grid

