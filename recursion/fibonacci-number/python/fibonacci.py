from typing import Dict

class Solution:
    def fib(self, n: int) -> int:
        d = {0: 0, 1: 1}
        return self._fib(n, d)

    def _fib(self, n: int, d: Dict) -> int:
        if d.get(n) is not None:
            return d[n]

        v = self._fib(n-1, d) + self._fib(n-2, d)

        d[n] = v

        return v
