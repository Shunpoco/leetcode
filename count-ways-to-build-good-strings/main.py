from typing import List, Dict

class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        mod = 1000000007
        memo = dict()
        self.exec(low, high, zero, one, mod, memo)

        return memo[(low, high)]

    def exec(self, low: int, high: int, zero: int, one: int, mod: int, memo: Dict[Tuple[int, int], int]) -> int:
        if memo.get((low, high)) is not None:
            return memo[(low, high)]

        r = 0

        if low <= 0:
            r += 1

        if zero <= high:
            self.exec(low-zero, high-zero, zero, one, mod, memo)
            r += memo[(low-zero, high-zero)]
            r %= mod

        if one <= high:
            self.exec(low-one, high-one, zero, one, mod, memo)
            r += memo[(low-one, high-one)]
            r %= mod

        memo[(low, high)] = r

        return

