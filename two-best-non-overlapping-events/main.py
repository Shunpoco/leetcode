class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort(key=lambda x: x[0])

        q = []

        mv = 0
        ms = 0

        for e in events:
            while len(q) > 0 and q[0][0] < e[0]:
                mv = max(mv, q[0][1])
                heapq.heappop(q)

            ms = max(ms, mv+e[2])

            heapq.heappush(q, (e[1], e[2]))

        return ms

