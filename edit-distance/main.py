
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
        
        for r in range(n+1):
            for c in range(m+1):
                if r == 0:
                    dp[r][c] = c
                elif c == 0:
                    dp[r][c] = r
                else:
                    v = 1
                    if word1[r-1] == word2[c-1]:
                        v = 0
                    dp[r][c] = min([dp[r-1][c]+1, dp[r][c-1]+1, dp[r-1][c-1]+v])
            
        return dp[n][m]
