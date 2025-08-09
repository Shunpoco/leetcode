class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        b = n.bit_count()

        return b == 1 and n > 0

