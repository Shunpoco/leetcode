class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        mod = 10 ** 9 + 7

        graph = [[] for _ in range(n)]

        for start, end, duration in roads:
            graph[start].append((end, duration))
            graph[end].append((start, duration))

        heap = [(0, 0)]
        shortest = [float('inf') for _ in range(n)]
        results = [0 for _ in range(n)]

        shortest[0] = 0
        results[0] = 1

        while len(heap) > 0:
            c_dur, c_node = heapq.heappop(heap)

            if c_dur > shortest[c_node]:
                continue

            for nei, dur in graph[c_node]:
                if c_dur + dur < shortest[nei]:
                    shortest[nei] = c_dur + dur
                    results[nei] = results[c_node]
                    heapq.heappush(heap, (shortest[nei], nei))

                elif c_dur + dur == shortest[nei]:
                    results[nei] = (results[nei] + results[c_node]) % mod

        return results[n-1]

