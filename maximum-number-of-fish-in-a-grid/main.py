class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        starts = []
        
        n = len(grid)
        m = len(grid[0])
        visited = [[False for _ in range(m)] for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if grid[i][j] > 0:
                    starts.append((i, j))
                else:
                    visited[i][j] = True

        result = 0
        for start in starts:
            if visited[start[0]][start[1]]:
                continue
            queue = [start]
            visited[start[0]][start[1]] = True
            t = 0
            while len(queue) > 0:
                v = queue.pop(0)
                t += grid[v[0]][v[1]]

                for d in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    i = v[0] + d[0]
                    j = v[1] + d[1]
                    
                    if i >= 0 and i < n and j >= 0 and j < m and grid[i][j] > 0 and not visited[i][j]:
                        queue.append((i, j))
                        visited[i][j] = True

            if t > result:
                result = t

        return result

