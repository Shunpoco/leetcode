from typing import List

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sort = self._sort(heights)

        r = 0
        for idx in range(len(heights)):
            if heights[idx] != sort[idx]:
                r += 1

        return r

    def _sort(self, nums: List[int]) -> List[int]:
        l = len(nums)

        if l <= 1:
            return nums

        m = int(l/2)

        right = self._sort(nums[:m])
        left = self._sort(nums[m:])

        r = []
        while len(right) > 0 or len(left) > 0:
            if len(right) == 0:
                r.append(left.pop(0))
                continue
            if len(left) == 0:
                r.append(right.pop(0))
                continue
            if right[0] > left[0]:
                r.append(left.pop(0))
            else:
                r.append(right.pop(0))

        return r
            