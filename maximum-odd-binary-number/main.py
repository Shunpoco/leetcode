class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        n = len(s)

        co = 0
        for c in s:
            if c == "1":
                co += 1

        result = "1" * (co-1) + "0" * (n-co) + "1"

        return result
