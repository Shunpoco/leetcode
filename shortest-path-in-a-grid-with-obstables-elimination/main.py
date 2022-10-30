from typing import List

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])
        
        if m == 1 and n == 1:
            return 0
        
        visit = set([(0,0,k)])
        q = [(0, 0, 0, k)] # y, x, steps, eraser
        
        if k > (m-1 + n-1):
            return m-1 + n-1
        
        while q:
            row, col, steps, eraser = q.pop(0)
            for new_row, new_col in [(row-1, col), (row, col+1), (row+1, col), (row, col-1)]:
                if (new_row >= 0 and new_row < m and new_col >= 0 and new_col < n):
                    if grid[new_row][new_col] == 1 and eraser > 0 and (new_row, new_col, eraser-1) not in visit:
                        visit.add((new_row, new_col, eraser-1))
                        q.append((new_row, new_col, steps+1, eraser-1))
                    if grid[new_row][new_col] == 0 and (new_row, new_col, eraser) not in visit:
                        if new_row == m-1 and new_col == n-1:
                            return steps+1
                        visit.add((new_row, new_col, eraser))
                        q.append((new_row, new_col, steps+1, eraser))
                        
        return -1
