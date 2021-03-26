class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        h = {}

        for x in s:
            if x in h.keys():
                h[x] += 1
            else:
                h[x] = 1

        for x in t:
            if x not in h.keys() or h[x] == 0:
                return False
            else:
                h[x] -= 1

        if sum(h.values()) != 0:
            return False

        return True
