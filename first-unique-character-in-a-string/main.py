class Solution:
    def firstUniqChar(self, s: str) -> int:
        memo1 = [-1 for _ in range(26)]
        memo2 = [0 for _ in range(26)]

        for i, c in enumerate(s):
            memo1[ord(c)-ord('a')] = i
            memo2[ord(c)-ord('a')] += 1

        r = -1
        for i in range(26):
            if memo2[i] == 1 and (r == -1 or r > memo1[i]):
                r = memo1[i]

        return r
