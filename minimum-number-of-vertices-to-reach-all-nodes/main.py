from typing import List
from collections import defaultdict

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        vertices = defaultdict(list)

        for edge in edges:
            f, t = edge[0], edge[1]
            vertices[t].append(f)

        result = list()
        for i in range(n):
            if vertices.get(i) is None:
                result.append(i)

        return result
