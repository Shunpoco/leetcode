class Solution:
    def makeFancyString(self, s: str) -> str:
        result = ""
        count = 0

        for c in s:
            if result == "" or result[-1] == c:
                if count < 2:
                    count += 1
                    result += c
            else:
                count = 1
                result += c

        return result

