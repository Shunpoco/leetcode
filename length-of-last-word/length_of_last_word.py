class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n = len(s)

        c = 0
        for i in range(n-1, -1, -1):
            if s[i] != ' ':
                c += 1
            elif c != 0:
                return c

        return c

