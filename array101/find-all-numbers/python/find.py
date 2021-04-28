from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        a = set(range(1, len(nums)+1))
        b = set(nums)

        return list(a^b)
