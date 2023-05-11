from typing import List

class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        dp = [[0 for _ in range(len(nums2)+1)] for _ in range(len(nums1)+1)]

        for i in range(len(nums1)+1):
            for j in range(len(nums2)+1):
                if i == 0 or j == 0:
                    dp[i][j] = 0
                elif nums1[i-1] == nums2[j-1]:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j-1]+1, dp[i-1][j])
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j-1], dp[i-1][j])

        return dp[len(nums1)][len(nums2)]

