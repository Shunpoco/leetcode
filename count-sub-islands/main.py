class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m, n = len(grid2), len(grid2[0])
        
        islands2 = []

        visited = [[False for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if not visited[i][j]:
                    visited[i][j] = True
                    q = [(i, j)]
                    t = []
                    while len(q):
                        cur = q.pop(0)
                        if grid2[cur[0]][cur[1]] == 1:
                            t.append((cur[0], cur[1]))
                            for di, dj in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                                if cur[0] + di < m and cur[0] + di >= 0 and cur[1] + dj < n and cur[1] + dj >= 0 and not visited[cur[0]+di][cur[1]+dj]:
                                    visited[cur[0]+di][cur[1]+dj] = True
                                    q.append((cur[0]+di, cur[1]+dj))

                    if len(t) > 0:
                        islands2.append(t)

        result = 0
        for land in islands2:
            t = len(land)
            for i, j in land:
                if grid1[i][j] == 1:
                    t -= 1
                else:
                    break
            if t == 0:
                result += 1

        return result
