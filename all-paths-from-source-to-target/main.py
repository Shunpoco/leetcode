from typing import List

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        q = [[0]]
        r = []

        while len(q) > 0:
            v = q.pop(0)
            if v[-1] == n-1:
                r.append(v)
            else:
                for e in graph[v[-1]]:
                    t = v.copy()
                    t.append(e)
                    q.append(t)

        return r
