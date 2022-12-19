from typing import List

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        visited = [False for _ in range(n)]
        queue = [source]
        visited[source] = True
        full_edges = [[] for _ in range(n)]
        for edge in edges:
            full_edges[edge[0]].append(edge[1])
            full_edges[edge[1]].append(edge[0])

        while len(queue) > 0:
            v = queue.pop(0)
            if v == destination:
                return True
            visited[v] = True
            for edge in full_edges[v]:
                if not visited[edge]:
                    queue.append(edge)

        return False
