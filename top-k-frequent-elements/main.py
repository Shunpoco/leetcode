import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter()
        for num in nums:
            cnt[num] += 1

        hq = []
        for n, c in cnt.items():
            heapq.heappush(hq, (-c, n))

        result = []
        for _ in range(k):
            result.append(heapq.heappop(hq)[1])

        return result

