from typing import List

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        return nums[self.exec(nums, 0, len(nums)-1)]

    def exec(self, nums, start, end) -> int:
        if start == end:
            return start

        m = (start+end)//2

        if nums[m] == nums[m+1] and (end-m)%2 == 0:
            return self.exec(nums, m+2, end)
        elif nums[m] != nums[m+1] and (end-m)%2 != 0:
            return self.exec(nums, m+1, end)

        if nums[m-1] == nums[m] and (m-start)%2 == 0:
            return self.exec(nums, start, m-2)
        elif nums[m-1] != nums[m+1] and (end-m)%2 != 0:
            return self.exec(nums, start, m-1)

        return m
