class Solution:
    def longestPalindrome(self, s: str) -> int:
        memo = defaultdict(int)

        for c in s:
            memo[c] += 1

        r = 0
        a = False
        for k, v in memo.items():
            if v % 2 == 0:
                r += v
            elif not a:
                r += v
                a = True
            else:
                r += v - 1

        return r

