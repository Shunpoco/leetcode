class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        start = 0
        result = 0

        for c in s:
            if c == "(":
                start += 1

            else:
                if start > 0:
                    start -= 1
                else:
                    result += 1

        return result + start
