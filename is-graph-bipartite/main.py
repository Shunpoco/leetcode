from typing import List

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        colors = [0 for _ in range(n)]
        
        for i in range(n):
            if colors[i] > 0:
                continue
            colors[i] = 1
            stack = [i]
            while len(stack) > 0:
                node = stack.pop(-1)
                color = 1 if colors[node] == 2 else 2

                for adj in graph[node]:
                    if colors[adj] == 0:
                        colors[adj] = color
                        stack.append(adj)
                    elif colors[adj] != color:
                        return False

        return True

