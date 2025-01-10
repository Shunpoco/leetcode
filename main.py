class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        def count(word):
            r = [0] * 26
            for c in word:
                r[ord(c)-ord('a')] += 1

            return r

        bs = [0]*26
        for word2 in words2:
            for i, c in enumerate(count(word2)):
                bs[i] = max(bs[i], c)

        result = []

        for word1 in words1:
            if all(x >= y for x, y in zip(count(word1), bs)):
                result.append(word1)

        return result

