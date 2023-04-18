
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ['' for _ in range(len(word1)+len(word2))]
        idx = 0
        idx1 = 0
        idx2 = 0
        while idx1 < len(word1) and idx2 < len(word2):
            result[idx] = word1[idx1]
            idx += 1
            idx1 += 1
            result[idx] = word2[idx2]
            idx += 1
            idx2 += 1

        while idx1 < len(word1):
            result[idx] = word1[idx1]
            idx += 1
            idx1 += 1

        while idx2 < len(word2):
            result[idx] = word2[idx2]
            idx += 1
            idx2 += 1

        return ''.join(result)

