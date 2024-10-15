class Solution:
    def minimumSteps(self, s: str) -> int:
        start = 0
        while start < len(s) and s[start] == '0':
            start += 1
        if start == len(s):
            return 0

        s = s[start:]

        end = len(s)
        while end >= 0 and s[end-1] == '1':
            end -= 1

        if end == 0:
            return 0

        s = s[:end]

        result = 0
        t = 0
        for c in s:
            if c == '0':
                result += t
            else:
                t += 1

        return result
