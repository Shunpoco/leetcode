class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        memo = [0, 0, 0] # a, b, c
        n = len(s)

        for c in s:
            memo[ord(c)-ord('a')] += 1

        for i in range(3):
            if memo[i] < k:
                return -1

        window = [0, 0, 0]
        l = 0
        max_window = 0

        for r in range(n):
            window[ord(s[r])-ord('a')] += 1

            while l <= r and (memo[0]-window[0] < k or memo[1]-window[1] < k or memo[2]-window[2] < k):
                window[ord(s[l])-ord('a')] -= 1
                l += 1

            max_window = max(max_window, r - l + 1)

        return n - max_window
