class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        hq = []

        for num in nums:
            heapq.heappush(hq, num)

        result = 0

        while len(hq) > 0:
            result += 1
            minv = heapq.heappop(hq)

            while len(hq) > 0 and hq[0] - minv <= k:
                heapq.heappop(hq)

        return result

