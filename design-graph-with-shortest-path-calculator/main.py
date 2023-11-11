from collections import defaultdict
from typing import List

class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.n = n
        self.edges = defaultdict(list)
        for edge in edges:
            self.edges[edge[0]].append((edge[1], edge[2]))
        

    def addEdge(self, edge: List[int]) -> None:
        self.edges[edge[0]].append((edge[1], edge[2]))

    def shortestPath(self, node1: int, node2: int) -> int:
        costs = [-1 for _ in range(self.n)]
        q = [node1]
        costs[node1] = 0

        while len(q) > 0:
            v = q.pop(0)

            if v == node2:
                continue

            for c in self.edges[v]:
                if costs[c[0]] == -1 or costs[v] + c[1] < costs[c[0]]:
                    costs[c[0]] = costs[v] + c[1]
                    q.append(c[0])

        return costs[node2]




# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)
