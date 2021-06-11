from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ht = {}

        for i in range(len(nums)):
            ht[nums[i]] = i

        for i in range(len(nums)):
            v = nums[i]
            j = ht.get(target-v)
            if j is not None and i != j:
                return [i, j]
