class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        memo1 = defaultdict(str)
        memo2 = defaultdict(str)

        for c1, c2 in zip(s, t):
            if memo1[c1] != '':
                if memo1[c1] != c2:
                    return False
            else:
                memo1[c1] = c2

            if memo2[c2] != '':
                if memo2[c2] != c1:
                    return False
            else:
                memo2[c2] = c1

        return True

