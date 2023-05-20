from typing import List
from collections import defaultdict

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        edges = defaultdict(list)

        for i, equation in enumerate(equations):
            edges[equation[0]].append((equation[1], 1/values[i]))
            edges[equation[1]].append((equation[0], values[i]))

        result = []
        for query in queries:
            a, b = query[0], query[1]
            if edges.get(a) is None or edges.get(b) is None:
                result.append(-1.0)
                continue
            elif a == b:
                result.append(1.0)
                continue

            adj = False
            visited = defaultdict(bool)
            visited[a] = True
            stack = [(a, 1.0)]
            while len(stack) > 0:
                node = stack.pop(-1)                
                for edge in edges[node[0]]:
                    if visited[edge[0]]:
                        continue
                    visited[edge[0]] = True
                    v = node[1]*edge[1]
                    if edge[0] == b:
                        result.append(1.0/v)
                        adj = True
                        break
                    stack.append((edge[0], v))

            if not adj:
                result.append(-1.0)

        return result

