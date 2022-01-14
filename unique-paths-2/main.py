from typing import List, Tuple, Dict

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        mem = {}
        
        return self.paths(obstacleGrid, 0, 0, mem)
    
    def paths(self, grid: List[List[int]], m: int, n: int, mem: Dict[Tuple[int, int], int]) -> int:        
        if mem.get((m, n)) is not None:
            return mem.get((m, n))
        
        lm = len(grid)
        ln = len(grid[0])

        if m >= lm or n >= ln or grid[m][n] == 1:
            v = 0
            
        elif m+1 == lm and n+1 == ln:
            v = 1
            
        else:
            v1 = self.paths(grid, m+1, n, mem)
            v2 = self.paths(grid, m, n+1, mem)
            
            v = v1 + v2
            
            
        mem[(m, n)] = v
        
        return v
