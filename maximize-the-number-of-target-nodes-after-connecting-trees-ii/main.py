class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        graph1 = defaultdict(list)
        graph2 = defaultdict(list)

        for e in edges1:
            graph1[e[0]].append(e[1])
            graph1[e[1]].append(e[0])

        for e in edges2:
            graph2[e[0]].append(e[1])
            graph2[e[1]].append(e[0])

        n = len(graph1.keys())
        m = len(graph2.keys())

        result = [0] * n

        # Graph1, Evaluate only node zero        
        q = [(0, 0)]
        visited = [False] * n
        visited[0] = True
        isEven = [False] * n
        c = 0

        while len(q) > 0:
            v = q.pop(0)
            if v[1] % 2 == 0:
                c += 1
                isEven[v[0]] = True

            for nex in graph1[v[0]]:
                if not visited[nex]:
                    q.append((nex, v[1]+1))
                    visited[nex] = True

        for i in range(n):
            if isEven[i]:
                result[i] = c
            else:
                result[i] = n - c

        # Graph2. Evaluate only node zero
        q = [(0, 0)]
        c_odd = 0
        c_even = 0
        visited = [False] * m
        visited[0] = True

        while len(q) > 0:
            v = q.pop(0)
            if v[1] % 2 == 0:
                c_even += 1
            else:
                c_odd += 1

            for nex in graph2[v[0]]:
                if not visited[nex]:
                    q.append((nex, v[1]+1))
                    visited[nex] = True

        mm = max(c_odd, c_even)

        for i in range(n):
            result[i] += mm

        return result

