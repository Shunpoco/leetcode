class Solution:
    def totalMoney(self, n: int) -> int:
        result = 0

        a = 0
        r = 0
        for i in range(n):
            if i % 7 == 0:
                a += 1
                r = a
            else:
                r += 1
            result += r

        return result
