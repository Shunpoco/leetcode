class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        c1 = num1.bit_count()
        c2 = num2.bit_count()

        if c1 == c2:
            return num1

        if c1 > c2:
            r = num1
            d = c1 - c2

            t = 1
            while d > 0:
                if num1 & t == t or t > num1:
                    r ^= t
                    d -= 1
                t <<= 1

            return r

        if c1 < c2:
            r = num1
            d = c2 - c1

            t = 1
            while d > 0:
                if num1 & t == 0:
                    r ^= t
                    d -= 1
                t <<= 1

            return r


