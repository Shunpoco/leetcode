class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        pq = []

        for gift in gifts:
            heapq.heappush(pq, -gift)

        for _ in range(k):
            v = -heapq.heappop(pq)

            t = 1
            while t * t <= v:
                t += 1
            t -= 1

            heapq.heappush(pq, -t)

        return -sum(pq)
