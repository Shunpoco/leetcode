import heapq
from typing import List

class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        q = [(-nums[n-1], n-1)]

        result = -q[0][0]
        for i in range(n-2, -1, -1):
            v = nums[i]
            m = -q[0][0] + v
            heapq.heappush(q, (-m, i))
            heapq.heappush(q, (-v, i))

            while i > 0 and q[0][1] - i >= k:
                heapq.heappop(q)

            if -q[0][0] > result:
                result = -q[0][0]

        return result

