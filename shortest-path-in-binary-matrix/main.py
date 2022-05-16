class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        visit = [];
        for _ in range(len(grid)):
            t = [0]*len(grid[0])
            visit.append(t)
        visit[0][0] = 1
        
        n = len(grid)
        
        queue = [(0, 0)]
        
        while len(queue) > 0:
            x, y = queue.pop(0)
            
            if grid[x][y] == 1:
                visit[x][y] = -1
                continue
            
            for i in [-1, 0, 1]:
                for j in [-1, 0, 1]:
                    if x+i >= 0 and x+i < n and y+j >= 0 and y+j < n:
                        if visit[x+i][y+j] == -1:
                            continue
                        if visit[x+i][y+j] == 0 or visit[x+i][y+j] > visit[x][y]+1:
                            visit[x+i][y+j] = visit[x][y]+1
                            queue.append((x+i, y+j))
                            
        r = visit[n-1][n-1]
        
        if r == 0:
            return -1
        return r
