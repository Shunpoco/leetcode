from typing import List

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        es = [(v[2], i, v[0], v[1]) for i, v in enumerate(edges)]
        es.sort()

        m = 0
        buf = UnionFind(n)
        for w, _, x, y in es:
            if buf.union(x, y):
                m += w
            if buf.ms == n:
                break
        
        cs = []
        pcs = []
        for wi, i, xi, yi in es:
            uf = UnionFind(n)
            t = 0
            for wj, j, xj, yj in es:
                if i == j:
                    continue
                if uf.union(xj, yj):
                    t += wj
                if uf.ms == n:
                    break
            # Critical
            if uf.ms != n or t > m:
                cs.append(i)
                continue
            
            uf = UnionFind(n)
            t = wi
            uf.union(xi, yi)
            for wj, j, xj, yj in es:
                if i == j:
                    continue
                if uf.union(xj, yj):
                    t += wj
                if uf.ms == n:
                    break
            
            # Pseudo-critical
            if uf.ms == n and t == m:
                pcs.append(i)

        return [cs, pcs]




class UnionFind:
    def __init__(self, n: int):
        self.p = [i for i in range(n)]
        self.s = [1 for _ in range(n)]
        self.ms = 1

    def find(self, x: int) -> int:
        if x != self.p[x]:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x: int, y: int) -> bool:
        px = self.find(x)
        py = self.find(y)

        if px != py:
            if self.s[px] < self.s[py]:
                px, py = py, px

            self.p[py] = px
            self.s[px] += self.s[py]
            self.ms = max(self.ms, self.s[px])
            return True

        return False


