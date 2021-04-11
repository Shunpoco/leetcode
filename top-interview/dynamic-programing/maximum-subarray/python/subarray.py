# isn't completed
from typing import List, Dict, Tuple

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        h = {}
        return self._max(nums, h, tuple([x for x in range(len(nums))]))

    def _max(self, nums: List[int], h: Dict, idx: Tuple[int]) -> int:
        if h.get(idx) is not None:
            return h.get(idx)
        if len(idx) == 1:
            h[idx] = nums[idx[0]]
            return h[idx]

        m = int(len(idx) / 2)
        r = self._max(nums, h, idx[0:m]) + self._max(nums, h, idx[m:])
        h[idx] = r
        return r

