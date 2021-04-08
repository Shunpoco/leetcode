class Solution:
    def __init__(self):
        self.DIGITS = {
            '0': 0,
            '1': 1,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9,
        }
        self.WHITE_SPACE = ' '
        self.NEGATIVE = '-'
        self.POSITIVE = '+'
        self.MAX = 2**31-1
        self.MIN = -2**31

    def myAtoi(self, s: str) -> int:
        r = 0
        start_digit = False
        code = 1
        for c in s:
            if start_digit:
                if self.DIGITS.get(c) is None:
                    break
                r *= 10
                r += self.DIGITS[c]

            else:
                if self.DIGITS.get(c) is not None:
                    start_digit = True
                    r = self.DIGITS[c]
                    continue
                if c == self.WHITE_SPACE:
                    continue
                if c == self.NEGATIVE:
                    start_digit = True
                    code = -1
                    continue
                if c == self.POSITIVE:
                    start_digit = True
                    continue
                else:
                    break

        r = r * code

        if r < self.MIN:
            return self.MIN
        if r > self.MAX:
            return self.MAX

        return r
