from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.exec(nums, target, 0, len(nums))

    def exec(self, nums, target, start, end) -> int:
        if start == end:
            return -1

        m = (start+end) // 2

        if nums[m] == target:
            return m

        elif nums[m] < target:
            return self.exec(nums, target, m+1, end)

        return self.exec(nums, target, start, m)

