class Solution:
    def longestPalindrome(self, s: str) -> str:
        p = ''

        for i in range(len(s)):
            p1 = self._palindrome(s, i, i+1)
            p2 = self._palindrome(s, i, i)

            p = max([p, p1, p2], key=lambda x: len(x))


        return p
    
    def _palindrome(self, s: str, left: int, right: int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1

        return s[left+1:right]
