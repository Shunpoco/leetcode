class Solution:
    MAX = 2147483647
    MIN = -2147483648
    def reverse(self, x:int) -> int:
        c = 1
        if x < 0:
            c = -1
            x *= -1

        r = 0
        i = 0
        while x != 0:
            v = x % 10
            x = int(x / 10)
            if i != 0 or v != 0:
                if i > 0:
                    r *= 10
                r += v
                i += 1

        r *= c

        if r < self.MIN or r > self.MAX:
            r = 0
                
        return r
