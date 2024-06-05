class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        n = len(words)

        counter = [[0 for _ in range(26)] for _ in range(n)]

        for i, word in enumerate(words):
            for c in word:
                counter[i][ord(c)-ord('a')] += 1

        result = []
        for i in range(26):
            t = float('inf')
            for j in range(n):
                t = min(t, counter[j][i])

            for j in range(t):
                result.append(chr(i+ord('a')))            

        return result

