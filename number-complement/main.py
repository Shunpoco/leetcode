class Solution:
    def findComplement(self, num: int) -> int:
        x = num
        y = 1

        while x > 0:
            num ^= y
            y <<= 1
            x >>= 1

        return num
