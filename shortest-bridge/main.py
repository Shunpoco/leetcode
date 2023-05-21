class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        island = [
            {},
            {}
        ]
        n = len(grid)

        ind = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1 and island[0].get((i, j)) is None and island[1].get((i, j)) is None:
                    stack = [(i, j)]

                    while len(stack) > 0:
                        row, col = stack.pop(-1)
                        island[ind][(row, col)] = 1

                        if row > 0 and island[ind].get((row-1, col)) is None and grid[row-1][col] == 1:
                            stack.append((row-1, col))
                        if row < n-1 and island[ind].get((row+1, col)) is None and grid[row+1][col] == 1:
                            stack.append((row+1, col))                        
                        if col > 0 and island[ind].get((row, col-1)) is None and grid[row][col-1] == 1:
                            stack.append((row, col-1))
                        if col < n-1 and island[ind].get((row, col+1)) is None and grid[row][col+1] == 1:
                            stack.append((row, col+1))
                    
                    ind = 1
        
        result = 1000000000
        for one in island[0].keys():
            for two in island[1].keys():
                diff = abs(one[0]-two[0]) + abs(one[1]-two[1]) - 1
                if result > diff:
                    result = diff

        return result
