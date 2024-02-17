# This is imcomplete

import heapq

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        h = []

        idx = 1
        c = 0
        while idx < len(heights):
            print(c)
            diff = heights[idx] - heights[idx-1]
            if diff <= 0:
                idx += 1
                continue

            if c + diff <= bricks:
                heapq.heappush(h, diff)
                c += diff
            else:
                if ladders > 0:
                    ladders -= 1
                    if len(h) > 0:
                        v = h[0]
                        if v > diff:
                            heapq.heappop(h)
                            c -= v
                            c += diff
                            heapq.heappush(h, diff)
                else:
                    break

            idx += 1

        return idx - 1
