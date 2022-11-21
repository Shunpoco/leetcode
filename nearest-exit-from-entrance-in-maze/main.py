from typing import List

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        nrow, ncol = len(maze), len(maze[0])
        
        queue = [(entrance[0], entrance[1], 0)]
        visited = [[False for _ in range(ncol)] for _ in range(nrow)]
        visited[entrance[0]][entrance[1]] = True
        while len(queue) > 0:
            r, c, s = queue.pop(0)
            if self.isExit(r, c, nrow, ncol) and (r != entrance[0] or c != entrance[1]):
                return s
            
            if r > 0 and maze[r-1][c] != "+" and not visited[r-1][c]:
                queue.append((r-1, c, s+1))
                visited[r-1][c] = True
            if r < nrow-1 and maze[r+1][c] != "+" and not visited[r+1][c]:
                queue.append((r+1, c, s+1))
                visited[r+1][c] = True
            if c > 0 and maze[r][c-1] != "+" and not visited[r][c-1]:
                queue.append((r, c-1, s+1))
                visited[r][c-1] = True
            if c < ncol-1 and maze[r][c+1] != "+" and not visited[r][c+1]:
                queue.append((r, c+1, s+1))
                visited[r][c+1] = True
                
        return -1
    
    
    
    def isExit(self, row: int, col: int, nrow: int, ncol: int) -> bool:
        if row == 0 or row == nrow-1 or col == 0 or col == ncol-1:
            return True
        return False
