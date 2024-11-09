class Solution:
    def minEnd(self, n: int, x: int) -> int:
        result = x
        n -= 1
        m = 1

        while n > 0:
            if (m & x) == 0:
                result |= (n&1) * m
                n >>= 1
            m <<= 1

        return result
