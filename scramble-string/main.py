from typing import List, Dict

class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        m = {}
        return self.exec(s1, s2, m)
    def exec(self, s1: str, s2: str, m: Dict) -> bool:
        n = len(s1)

        if m.get((s1, s2)) is not None:
            return m[(s1, s2)]

        if n == 1:
            return s1 == s2

        for i in range(1, n):
            v1, v2 = s1[:i], s1[i:]

            r = self.exec(v1, s2[:i], m) & self.exec(v2, s2[i:], m) | self.exec(v2, s2[:len(v2)], m) & self.exec(v1, s2[len(v2):], m)

            if r:
                break

        m[(s1, s2)] = r

        return r
