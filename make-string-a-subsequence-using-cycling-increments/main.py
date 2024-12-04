class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        A = ord('a')
        mod = 26

        str1d = ""
        for c in str1:
            v = (ord(c) - A + 1) % mod + A
            str1d += chr(v)

        idx = 0
        for c1, c1d in zip(str1, str1d):
            if c1 == str2[idx] or c1d == str2[idx]:
                idx += 1

            if idx == len(str2):
                return True

        return False

