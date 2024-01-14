class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        memo1 = defaultdict(int)
        memo2 = defaultdict(int)

        for c1, c2 in zip(word1, word2):
            memo1[c1] += 1
            memo2[c2] += 1

        k1 = list(memo1.keys())
        k1.sort()

        k2 = list(memo2.keys())
        k2.sort()

        if k1 != k2:
            return False

        v1 = list(memo1.values())
        v1.sort()

        v2 = list(memo2.values())
        v2.sort()

        return v1 == v2
