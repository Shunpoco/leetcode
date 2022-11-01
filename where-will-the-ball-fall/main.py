from typing import List

class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m = len(grid)
        n = len(grid[0])
        
        result = [-1 for _ in range(n)]
        for i in range(n):
            cpos = i
            f = True
            for j in range(m):
                direction = grid[j][cpos]
                
                if direction == -1 and cpos == 0:
                    adj = 1
                elif direction == 1 and cpos == n-1:
                    adj = -1
                elif direction == -1:
                    adj = grid[j][cpos-1]
                else:
                    adj = grid[j][cpos+1]
                    
                if direction != adj:
                    f = False
                    break
                
                if direction == 1:
                    cpos += 1
                else:
                    cpos -= 1
                    
            if f:
                result[i] = cpos

        return result
