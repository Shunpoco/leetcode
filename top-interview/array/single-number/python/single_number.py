from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return 2 * sum(set(nums)) - sum(nums)

    def singleNumber_hash(self, nums: List[int]) -> int:
        h = {}
        r = 0
        for num in nums:
            if h.get(num) is None:
                h[num] = 1
                r += num
            else:
                r -= num

        return r
