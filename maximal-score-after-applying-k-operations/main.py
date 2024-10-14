class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        pq = []
        for num in nums:
            heapq.heappush(pq, -num)

        result = 0
        for _ in range(k):
            v = -heapq.heappop(pq)

            result += v

            if v % 3 == 0:
                v = v // 3
            else:
                v = v // 3 + 1

            heapq.heappush(pq, -v)

        return result
