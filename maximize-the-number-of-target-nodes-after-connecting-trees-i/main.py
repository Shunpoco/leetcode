class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        graph1 = defaultdict(list)
        graph2 = defaultdict(list)

        for edge in edges1:
            graph1[edge[0]].append(edge[1])
            graph1[edge[1]].append(edge[0])

        for edge in edges2:
            graph2[edge[0]].append(edge[1])
            graph2[edge[1]].append(edge[0])
        
        n = max(list(graph1.keys())) + 1
        m = max(list(graph2.keys())) + 1

        depth1 = [0] * n
        for i in range(n):
            t = [False] * n
            t[i] = True
            c = 0
            q = [(i, 0)]

            while len(q) > 0:
                v = q.pop(0)
                c += 1
                if v[1] == k:
                    continue
                for nex in graph1[v[0]]:
                    if not t[nex]:
                        q.append((nex, v[1]+1))
                        t[nex] = True

            depth1[i] = c


        depth2 = [0] * m
        if k > 0:
            for i in range(m):
                t = [False] * m
                t[i] = True
                c = 0
                q = [(i, 0)]

                while len(q) > 0:
                    v = q.pop(0)
                    c += 1
                    if v[1] == k-1:
                        continue
                    for nex in graph2[v[0]]:
                        if not t[nex]:
                            q.append((nex, v[1]+1))
                            t[nex] = True

                depth2[i] = c

        max2 = max(depth2)

        result = []

        for i in range(n):
            result.append(depth1[i]+max2)

        return result


