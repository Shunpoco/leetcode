from typing import List

class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n = len(edges)
        distances1 = [-1 for _ in range(n)]
        
        visited = [False for _ in range(n)]
        queue = [node1]
        visited[node1] = True
        distances1[node1] = 0
        p = 0
        while len(queue) > 0:
            node = queue.pop(0)
            edge = edges[node]
            p += 1
            if edge != -1 and not visited[edge]:
                queue.append(edge)
                visited[edge] = True
                if p > distances1[edge]:
                    distances1[edge] = p

        distances2 = [-1 for _ in range(n)]
        visited = [False for _ in range(n)]
        queue = [node2]
        visited[node2] = True
        distances2[node2] = 0
        p = 0
        while len(queue) > 0:
            node = queue.pop(0)
            edge = edges[node]
            p += 1
            if edge != -1 and not visited[edge]:
                queue.append(edge)
                visited[edge] = True
                if p > distances2[edge]:
                    distances2[edge] = p
        
        mins = 99999999999999999
        result = -1
        for i, (a, b) in enumerate(zip(distances1, distances2)):
            if a >= 0 and b >= 0 and max(a, b) < mins:
                mins = max(a, b)
                result = i            

        return result
