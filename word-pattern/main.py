class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        ss = s.split(" ")
        if len(pattern) != len(ss):
            return False
        memo1 = {}
        memo2 = {}

        for p, w in zip(pattern, ss):
            if memo1.get(p) is not None and memo1[p] != w:
                return False
            if memo2.get(w) is not None and memo2[w] != p:
                return False
            memo1[p] = w
            memo2[w] = p

        return True
