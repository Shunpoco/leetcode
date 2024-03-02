class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        q = []

        for num in nums:
            heapq.heappush(q, num**2)

        result = []
        while len(q) > 0:
            result.append(heapq.heappop(q))

        return result
