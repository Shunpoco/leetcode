class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        c = 0

        for i in range(len(s) // 2):
            if s[i] in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
                c += 1

        for i in range(len(s) // 2, len(s)):
            if s[i] in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
                c -= 1

        return c == 0
