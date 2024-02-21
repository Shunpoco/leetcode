class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        r = 0

        while left > 0 and right > 0:
            b = 1
            while b <= left:
                b *= 2
            if b > left:
                b //= 2
            if b*2 <= right:
                break

            r += b
            left -= b
            right -= b

        return r
