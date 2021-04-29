from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[i] = nums[i] * nums[i]

        return self._sort(nums)

    def _sort(self, nums: List[int]) -> List[int]:
        l = len(nums)

        if l <= 1:
            return nums

        m = int(l/2)

        left = self._sort(nums[:m])
        right = self._sort(nums[m:])

        r = []

        while len(left) > 0 or len(right) > 0:
            if len(left) == 0:
                r.append(right.pop(0))
                continue
            if len(right) == 0:
                r.append(left.pop(0))
                continue

            if left[0] > right[0]:
                r.append(right.pop(0))
            else:
                r.append(left.pop(0))

        return r
