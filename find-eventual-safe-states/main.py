from typing import List

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        
        safes = [False for _ in range(n)]
        visited = [False for _ in range(n)]

        for i in range(n):
            if not visited[i]:
                visited[i] = True
                self.search(i, graph, safes, visited)

        result = []

        for i, v in enumerate(safes):
            if v:
                result.append(i)

        return result

    def search(self, i: int, graph: List[List[int]], safes: List[bool], visited: List[bool]):
        g = graph[i]

        if len(g) == 0:
            safes[i] = True
            return

        r = True
        for nex in g:
            if not visited[nex]:
                visited[nex] = True
                self.search(nex, graph, safes, visited)

            r &= safes[nex]

        safes[i] = r

        return
