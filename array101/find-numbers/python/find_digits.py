from typing import List

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        r = 0
        for num in nums:
            n = self._nDigits(num)
            if n % 2 == 0:
                r += 1
        return r

    def _nDigits(self, num: int) -> int:
        n = 0
        while num > 0:
            n += 1
            num = int(num / 10)
        return n
