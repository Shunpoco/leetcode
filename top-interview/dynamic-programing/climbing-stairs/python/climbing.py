from typing import Dict

class Solution:
    def climbStairs(self, n: int) -> int:
        h = {0: 1, 1: 1}
        return self._climbs(n, h)

    def _climbs(self, n: int, h: Dict) -> int:
        r = h.get(n)
        if r is not None:
            return r

        r = self._climbs(n-1, h) + self._climbs(n-2, h)

        h[n] = r

        return r
