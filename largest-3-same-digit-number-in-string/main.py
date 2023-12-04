class Solution:
    def largestGoodInteger(self, num: str) -> str:
        result = ""

        cur = ""
        count = 0

        for n in num:
            if cur == n:
                count += 1
            else:
                cur = n
                count = 1

            if count == 3:
                t = n + n + n
                if result < t:
                    result = t

        return result
