class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        result = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    result += self.nums(grid, (i,j))
                    
        return result

    def nums(self, grid, pos) -> int:
        print(pos)
        count = 0
        if pos[0] == 0 or grid[pos[0]-1][pos[1]] == 0:
            count += 1
        if pos[0] == len(grid)-1 or grid[pos[0]+1][pos[1]] == 0:
            count += 1
        if pos[1] == 0 or grid[pos[0]][pos[1]-1] == 0:
            count += 1
        if pos[1] == len(grid[0])-1 or grid[pos[0]][pos[1]+1] == 0:
            count += 1
            
        return count
