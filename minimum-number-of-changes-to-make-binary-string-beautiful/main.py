class Solution:
    def minChanges(self, s: str) -> int:
        result = 0

        idx = 0

        while idx < len(s):
            if s[idx] != s[idx+1]:
                result += 1

            idx += 2

        return result

