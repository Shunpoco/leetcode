from typing import List

import heapq

class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        a = []
        b = []

        for n1, n2 in zip(nums1, nums2):
            heapq.heappush(a, (-n1, -n2))

        sums = 0
        mins = 100000000
        for _ in range(k):
            n1, n2 = heapq.heappop(a)
            heapq.heappush(b, (-n2, -n1))
            sums -= n1
            if mins > -n2:
                mins = -n2

        result = sums * mins

        while len(a) > 0:
            n2, n1 = heapq.heappop(b)
            sums -= n1
            n1, n2 = heapq.heappop(a)
            sums -= n1
            heapq.heappush(b, (-n2, -n1))
            mins = b[0][0]

            if result < sums*mins:
                result = sums*mins

        return result

