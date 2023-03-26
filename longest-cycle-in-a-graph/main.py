from typing import List

class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        n = len(edges)
        result = -1
        visited = [False for _ in range(n)]
        candidates = []
        for i, v in enumerate(edges):
            if v == -1:
                visited[i] = True
            else:
                candidates.append(i)


        for cur in candidates:
            if not visited[cur]:
                route = {}
                visited[cur] = True
                route[cur] = 0
                while edges[cur] > -1:
                    nex = edges[cur]
                    if visited[nex]:
                        if route.get(nex) is not None:
                            result = max(result, (route[cur]+1) - route[nex])
                        break
                    visited[nex] = True
                    route[nex] = route[cur] + 1
                    cur = nex

        return result
