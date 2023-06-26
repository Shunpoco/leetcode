from typing import List

import heapq

class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        pq = []

        left, right = 0, len(costs)-1

        for _ in range(candidates):
            if left > right:
                break
            heapq.heappush(pq, (costs[left], left, True))
            left += 1
            if left > right:
                break
            heapq.heappush(pq, (costs[right], right, False))
            right -= 1

        total = 0
        for _ in range(k):
            v, _, l = heapq.heappop(pq)
            total += v
            if l and left <= right:
                heapq.heappush(pq, (costs[left], left, True))
                left += 1
            elif not l and left <= right:
                heapq.heappush(pq, (costs[right], right, False))
                right -= 1

        return total
