class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        result = 0
        queue = []
        
        M = len(grid)
        N = len(grid[0])
        
        for i in range(M):
            for j in range(N):
                if grid[i][j] == '1':
                    # start BFS
                    result += 1
                    queue.append((i, j))
                    
                    while queue:
                        point = queue.pop(0)
                        
                        if grid[point[0]][point[1]] == '1':
                            grid[point[0]][point[1]] = '0'

                            if point[0] > 0:
                                queue.append((point[0]-1, point[1]))
                            if point[0] < M-1:
                                queue.append((point[0]+1, point[1]))
                            if point[1] > 0:
                                queue.append((point[0], point[1]-1))
                            if point[1] < N-1:
                                queue.append((point[0], point[1]+1))
                                
        return result

