class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False

        c = 0

        while n > 0:
            c += n & 1
            n >>= 1

        return c == 1
