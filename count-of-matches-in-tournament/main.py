class Solution:
    def numberOfMatches(self, n: int) -> int:
        result = 0
        while n > 1:
            if n % 2 == 1:
                result += (n-1) // 2
                n = (n-1) // 2 + 1
            else:
                result += n // 2
                n //= 2

        return result
