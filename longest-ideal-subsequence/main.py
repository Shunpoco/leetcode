class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        dp = [0 for _ in range(26)]

        result = 1

        for i in range(len(s)):
            c = ord(s[i]) - ord('a')

            j = c
            while j >= 0 and j >= c - k:
                dp[c] = max(dp[c], dp[j]+1)
                j -= 1

            j = c + 1
            while j < 26 and j <= c + k:
                dp[c] = max(dp[c], dp[j]+1)
                j += 1

            result = max(result, dp[c])

        return result

