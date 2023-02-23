from typing import List

import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        tasks = [(c, -p) for c, p in zip(capital, profits)]
        tasks.sort()

        heap = []
        for _ in range(k):
            if len(tasks) > 0:
                v = tasks[0]
                while v[0] <= w:
                    heapq.heappush(heap, v[1])
                    tasks.pop(0)
                    if len(tasks) == 0:
                        break
                    v = tasks[0]

            if len(heap) > 0:
                w += -1*heapq.heappop(heap)


        return w

