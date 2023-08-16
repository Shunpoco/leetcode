from collections import Counter
import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = []
        counter = Counter()

        r = []

        # initialize
        for i in range(k):
            heapq.heappush(q, -nums[i])
            counter[nums[i]] += 1
        r.append(-q[0])

        for i in range(k, len(nums)):
            prev = nums[i-k]
            counter[prev] -= 1
            while len(q) > 0 and counter[-q[0]] == 0:
                heapq.heappop(q)

            heapq.heappush(q, -nums[i])
            counter[nums[i]] += 1
            r.append(-q[0])

        return r

