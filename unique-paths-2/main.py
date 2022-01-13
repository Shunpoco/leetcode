class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        memory = {}
        
        return self.paths(obstacleGrid, 0, 0, memory)
    
    def paths(self, grid: List[List[int]], m: int, n: int, memory: Dict) -> int:
        if memory.get((m, n)) is not None:
            return memory.get((m, n))            

        if m >= len(grid) or n >= len(grid[0]) or grid[m][n] == 1:
            v = 0
        elif m+1 == len(grid) and n+1 == len(grid[0]):
            v = 1
        else:
            v1 = self.paths(grid, m+1, n, memory)
            v2 = self.paths(grid, m, n+1, memory)
            v = v1 + v2
                
        memory[(m, n)] = v
            
        return v
