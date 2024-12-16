class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        result = [0 for _ in range(len(nums))]

        pq = []

        for i, num in enumerate(nums):
            heapq.heappush(pq, (num, i))

        for _ in range(k):
            v = heapq.heappop(pq)

            heapq.heappush(pq, (v[0]*multiplier, v[1]))

        while len(pq) > 0:
            v = heapq.heappop(pq)

            result[v[1]] = v[0]

        return result

