import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]

# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         q = []

#         for num in nums:
#             heapq.heappush(q, -num)

#         r = 0
#         for _ in range(k):
#             r = -heapq.heappop(q)

#         return r
