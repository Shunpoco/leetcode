from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        nums = [x**2 for x in nums]
    
        return self._sort(nums)

    def _sort(self, nums: List[int]) -> List[int]:
        l = len(nums)

        if l == 1:
            return nums

        m = int(l/2)

        left = self._sort(nums[:m])
        right = self._sort(nums[m:])

        res = []

        while len(left) > 0 and len(right) > 0:
            if left[0] < right[0]:
                res.append(left[0])
                left.pop(0)
            else:
                res.append(right[0])
                right.pop(0)

        if len(left) > 0:
            res.extend(left)

        elif len(right) > 0:
            res.extend(right)

        return res
