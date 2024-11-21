class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [[0 for _ in range(n)] for _ in range(m)]

        for guard in guards:
            grid[guard[0]][guard[1]] = 2
        
        for wall in walls:
            grid[wall[0]][wall[1]] = 3

        for guard in guards:
            self.dfs(guard[0]-1, guard[1], grid, 0)
            self.dfs(guard[0]+1, guard[1], grid, 1)
            self.dfs(guard[0], guard[1]-1, grid, 2)
            self.dfs(guard[0], guard[1]+1, grid, 3)

        result = sum(row.count(0) for row in grid)

        return result

    def dfs(self, row, col, grid, direction):
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] in [2, 3]: # guard or wall
            return

        grid[row][col] = 1 # Guarded
        if direction == 0:
            self.dfs(row-1, col, grid, 0)
        if direction == 1:
            self.dfs(row+1, col, grid, 1)
        if direction == 2:
            self.dfs(row, col-1, grid, 2)
        if direction == 3:
            self.dfs(row, col+1, grid, 3)
