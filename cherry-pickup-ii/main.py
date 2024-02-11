class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        memo = {}

        self.solve(0, len(grid[0])-1, 0, grid, memo)

        return memo[(0, len(grid[0])-1, 0)]

    def solve(self, l, r, row, grid, memo):
        if memo.get((l, r, row)) is not None:
            return

        result = grid[row][l] + grid[row][r]
        if l == r:
            result = grid[row][l]

        if row == len(grid)-1:
            memo[(l, r, row)] = result
            return

        v = 0
        # Left robot
        for i in [-1, 0, 1]:
            # Right robot
            for j in [-1, 0, 1]:
                if (l + i >= 0 and l+i < len(grid[0])) and (r + j >= 0 and r + j < len(grid[0])):
                    self.solve(l+i, r+j, row+1, grid, memo)
                    t = memo[(l+i, r+j, row+1)]
                    if v < t:
                        v = t

        memo[(l, r, row)] = result + v

        return
