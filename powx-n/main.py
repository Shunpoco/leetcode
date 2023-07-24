from typing import List

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            n *= -1
            x = 1/x

        memo = {0: 1.0, 1: x}
        r = self.exec(x, n, memo)

        return r



    def exec(self, x: float, n: int, memo: Dict[int, float]):
        if memo.get(n) is not None:
            return memo[n]
    
        v = 1
        if n % 2 != 0:
            v = x
            n -= 1

        t = self.exec(x, n/2, memo)

        v *= t * t 

        memo[n] = v

        return v



