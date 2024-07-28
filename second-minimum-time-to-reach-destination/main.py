class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        graph = [[] for _ in range(n+1)]
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        dist1 = [float('inf') for _ in range(n+1)]
        dist2 = [float('inf') for _ in range(n+1)]
        freq = [0 for _ in range(n+1)]

        pq = []
        heapq.heappush(pq, (0, 1))
        dist1[1] = 0

        while len(pq) > 0:
            tt, node = heapq.heappop(pq)

            freq[node] += 1

            if freq[node] == 2 and node == n:
                return tt

            if (tt // change) % 2 == 1:
                tt = change * (tt // change + 1) + time
            else:
                tt += time

            for nei in graph[node]:
                if freq[nei] == 2:
                    continue

                if dist1[nei] > tt:
                    dist2[nei] = dist1[nei]
                    dist1[nei] = tt
                    heapq.heappush(pq, (tt, nei))
                elif dist2[nei] > tt and dist1[nei] != tt:
                    dist2[nei] = tt
                    heapq.heappush(pq, (tt, nei))

        return 0
