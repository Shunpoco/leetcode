
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        self.n = len(s)
        self.s = s

        for l in range(self.n//2, 0, -1):
            if self.n % l != 0:
                continue

            if self.check(l):
                return True

        return False

    def check(self, l: int) -> bool:
        d = self.n // l
        base = self.s[0:l]

        for i in range(1, d):
            if base != self.s[l*i:l*(i+1)]:
                return False

        return True
