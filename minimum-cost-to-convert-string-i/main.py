class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        table = [[float('inf') for _ in range(26)] for _ in range(26)]
        a = ord('a')

        for o, d, c in zip(original, changed, cost):
            if table[ord(o)-a][ord(d)-a] > c:
                table[ord(o)-a][ord(d)-a] = c

        min_costs = [self.dijkstra(i, table) for i in range(26)]

        result = 0
        for o, d in zip(source, target):
            if o == d:
                continue

            oi = ord(o)-a
            di = ord(d)-a

            v = min_costs[oi][di]
            if v == float('inf'):
                return -1

            result += v

        return result

    def dijkstra(self, oi, table) -> List[int]:
        pq = [(0, oi)]

        min_costs = [float('inf') for _ in range(26)]

        while len(pq) > 0:
            cc, ci = heapq.heappop(pq)

            if min_costs[ci] != float('inf'):
                continue

            min_costs[ci] = cc

            for tc, cost in enumerate(table[ci]):
                if cost != float('inf'):
                    newc = cc + cost

                    if min_costs[tc] == float('inf'):
                        heapq.heappush(pq, (newc, tc))

        return min_costs
