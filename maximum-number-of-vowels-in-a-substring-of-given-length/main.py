class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        bowels = ['a', 'e', 'i', 'o', 'u']
        r = 0
        result = 0

        for i in range(k):
            if s[i] in bowels:
                result += 1

        r = result
        for i in range(0, len(s)-k):
            if s[i] in bowels:
                result -= 1
            if s[i+k] in bowels:
                result += 1

            if r < result:
                r = result

        return r

