class Solution:
    def clearStars(self, s: str) -> str:
        memo = [[] for _ in range(26)]

        s = list(s)
        for i, c in enumerate(s):
            if c != '*':
                memo[ord(c)-ord('a')].append(i)
                continue

            for j in range(26):
                if len(memo[j]) > 0:
                    s[memo[j].pop()] = '*'
                    break

        return "".join(c for c in s if c != '*')

