class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        base = 65
        r = ""
        while columnNumber > 0:
            columnNumber -= 1

            r = chr(base + columnNumber % 26) + r
            columnNumber //= 26
        return r

