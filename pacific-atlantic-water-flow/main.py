
class Solution:
    def bfs(self, starts, H):
        n, m = len(H), len(H[0])
        queue = deque(starts)
        visited = set(starts)
        
        while queue:
            x, y = queue.popleft()
            for dx, dy in [(x, y+1), (x, y-1), (x-1, y), (x+1, y)]:
                withinBound = 0 <= dx < n and 0 <= dy < m
                notVisited = (dx, dy) not in visited
                if withinBound and notVisited and H[dx][dy] >= H[x][y]:
                    queue.append((dx, dy))
                    visited.add((dx, dy))
                    
        return visited
        
    def pacificAtlantic(self, H: List[List[int]]) -> List[List[int]]:
        if not H or not H[0]: return []
        n, m = len(H), len(H[0])
        
        pacific = [(0, i) for i in range(m)] + [(i, 0) for i in range(1, n)]
        athlantic = [(n-1, i) for i in range(m)] + [(i, m-1) for i in range(n-1)]
        
        return self.bfs(pacific, H) & self.bfs(athlantic, H)
