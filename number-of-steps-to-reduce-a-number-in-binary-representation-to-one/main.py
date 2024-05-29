class Solution:
    def numSteps(self, s: str) -> int:
        n = len(s)
        v = 0
        for i in range(n):
            if i != 0:
                v <<= 1
            if s[i] == "1":
                v += 1
        
        c = 0
        while v > 1:
            if v & 1 == 1:
                v += 1
            else:
                v >>= 1
            c += 1

        return c

