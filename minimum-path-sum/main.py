from typing import List, Tuple, Dict

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        mem = {}
        
        return self.minPath(grid, 0, 0, mem)
    
    def minPath(self, grid: List[List[int]], m: int, n: int, mem: Dict[Tuple[int, int], int]) -> int:
        if mem.get((m, n)) is not None:
            return mem.get((m, n))
        
        lm = len(grid)
        ln = len(grid[0])
        
        if m >= lm or n >= ln:
            result = inf
            
        elif m+1 == lm and n+1 == ln:
            result = grid[m][n]
            
        else:
            base = grid[m][n]
            result = base + self.minPath(grid, m+1, n, mem)
            v2 = base + self.minPath(grid, m, n+1, mem)
            
            if v2 < result:
                result = v2

        mem[(m, n)] = result
        
        return result
