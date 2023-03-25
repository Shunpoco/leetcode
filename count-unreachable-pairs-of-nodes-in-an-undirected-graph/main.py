from typing import List

class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)

        for edge in edges:
            uf.unite(*edge)

        for i in range(n):
            uf.root(i)

        d = defaultdict(int)
        for c in uf.par:
            d[c] += 1
        
        v = list(d.values())
        l = len(v)
        f = v[0]
        r = 0
        for i in range(1, l):
            r += f * v[i]
            f += v[i]

        return r


class UnionFind:
    def __init__(self, n: int):
        self.par = [i for i in range(n)]

    def root(self, x: int) -> int:
        if self.par[x] == x:
            return x

        self.par[x] = self.root(self.par[x])
        return self.par[x]

    def unite(self, x: int, y: int):
        rx = self.root(x)
        ry = self.root(y)

        if rx == ry:
            return
        
        if rx > ry:
            rx, ry = ry, rx
        self.par[ry] = rx

    
