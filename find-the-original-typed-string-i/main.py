class Solution:
    def possibleStringCount(self, word: str) -> int:
        result = 1

        prev = ""
        for c in word:
            if prev == c:
                result += 1
            else:
                prev = c
        return result

