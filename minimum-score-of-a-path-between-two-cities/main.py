from typing import List

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        paths = defaultdict(list)
        for road in roads:
            paths[road[0]].append((road[1], road[2]))
            paths[road[1]].append((road[0], road[2]))

        dis = [-1 for _ in range(n+1)]
        dis[0] = 0
        dis[1] = 99999999999

        print(paths)

        q = [1]
        while len(q) > 0:
            v = q.pop(0)
            d = dis[v]
            cs = paths[v]

            for c in cs:
                if dis[c[0]] == -1 or dis[c[0]] > min(d, c[1]):
                    dis[c[0]] = min(d, c[1])
                    q.append(c[0])

        print(dis)
        return dis[n]


