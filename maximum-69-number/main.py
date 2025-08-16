class Solution:
    def maximum69Number (self, num: int) -> int:
        t = num
        i = 1
        p = 0

        while t > 0:
            if t % 10 == 6:
                p = i

            t //= 10
            i *= 10

        return  num - 6 * p + 9 * p

