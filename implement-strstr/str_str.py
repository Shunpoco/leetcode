class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == '':
            return 0
        needleLen = len(needle)
        startNeedle = needle[0]
        for i in range(len(haystack)):
            if haystack[i] == startNeedle:
                substr = haystack[i:i+needleLen]
                if substr == needle:
                    return i
        return -1
