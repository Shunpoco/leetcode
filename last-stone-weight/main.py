class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        q = []

        for stone in stones:
            heapq.heappush(q, -stone)

        while len(q) > 1:
            x = -heapq.heappop(q)
            y = -heapq.heappop(q)

            if x > y:
                heapq.heappush(q, y-x)

        if len(q) == 1:
            return -q[0]

        return 0

