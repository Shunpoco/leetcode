from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = {}

        for x in nums:
            try:
                d[x]
                return True
            except:
                d[x] = 1

        return False
