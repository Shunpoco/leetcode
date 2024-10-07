class Solution:
    def minLength(self, s: str) -> int:
        i = 1
        while i > 0:
            i = 0

            for j in range(len(s)-1):
                if s[j:j+2] == "AB" or s[j:j+2] == "CD":
                    s = s[:j] + s[j+2:]
                    i = 1
                    break

        return len(s)
