class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        r = []
        for pile in piles:
            heapq.heappush(r, -pile)

        for _ in range(k):
            v = heapq.heappop(r)
            v = v // 2
            heapq.heappush(r, v)
        return sum(r) * -1
