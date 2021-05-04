class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n *= -1
        
        d = {0: 1.0, 1: x}
        return self._pow(x, n, d)

    def _pow(self, x: float, n: int, d) -> float:
        if d.get(n):
            return d.get(n)

        v = 1.0
        if n % 2 != 0:
            v *= x
            n = n - 1

        t = self._pow(x, n/2, d)
        v = v * t * t

        d[n] = v

        return v
