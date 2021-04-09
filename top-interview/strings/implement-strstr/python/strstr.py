class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == '':
            return 0

        lh = len(haystack)
        ln = len(needle)

        start = 0

        while start + ln <= lh:
            p = haystack[start:start+ln]
            if needle == p:
                return start
            start += 1

        return -1
