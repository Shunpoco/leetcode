# https://leetcode.com/problems/word-break/discuss/43995/A-Simple-Python-DP-solution
from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1) # dp[i] means s[:i+1] can be segmented into words in the wordDict
        dp[0] = True

        for i in range(len(s)):
            for j in range(i, len(s)):
                if dp[i] and s[i:j+1] in wordDict:
                    dp[j+1] = True


        return dp[-1]
