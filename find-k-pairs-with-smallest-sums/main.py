from collections import defaultdict
from typing import List

import heapq

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        result = []
        q = [(nums1[0]+nums2[0], 0, 0)]
        mem = defaultdict(bool)

        while len(result) < k and len(q) > 0:
            _, i1, i2 = heapq.heappop(q)
            if mem[(i1, i2)]:
                continue
            result.append([nums1[i1], nums2[i2]])

            if i1 < len(nums1)-1:
                heapq.heappush(q, (nums1[i1+1]+nums2[i2], i1+1, i2))
                heapq.heappush(q, (nums1[i1+1]+nums2[0], i1+1, 0))
            if i2 < len(nums2)-1:
                heapq.heappush(q, (nums1[i1]+nums2[i2+1], i1, i2+1))
                heapq.heappush(q, (nums1[0]+nums2[i2+1], 0, i2+1))

            mem[(i1, i2)] = True

        return result

