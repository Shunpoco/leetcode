from typing import List

class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        answer = []

        for l_, r_ in zip(l, r):
            q = []
            for t in nums[l_:r_+1]:
                heapq.heappush(q, t)

            prev = heapq.heappop(q)
            cur = heapq.heappop(q)
            diff = cur - prev

            prev = cur
            r = True
            while len(q):
                cur = heapq.heappop(q)

                if cur - prev != diff:
                    r = False
                    break
                prev = cur

            answer.append(r)

        return answer
