class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        memo = {}

        a = 0
        while a * a <= c:
            b2 = c - a * a

            if a*a == b2 or memo.get(a*a) is not None or memo.get(b2) is not None:
                return True


            memo[a*a] = True
            memo[b2] = True
            a += 1

        return False

