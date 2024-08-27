class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        paths = defaultdict(list)

        for edge, prob in zip(edges, succProb):
            paths[edge[0]].append((edge[1], prob))
            paths[edge[1]].append((edge[0], prob))

        res = [0.0 for _ in range(n)]
        res[start_node] = 1.0

        q = [start_node]

        while len(q):
            v = q.pop(0)
            
            for p in paths[v]:
                t = res[v] * p[1]

                if t > res[p[0]]:
                    res[p[0]] = t
                    q.append(p[0])

        return res[end_node]
