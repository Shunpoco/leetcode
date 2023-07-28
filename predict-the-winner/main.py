from typing import List

class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [[-1 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if j < i:
                    dp[i][j] = 0
                elif j == i:
                    dp[i][j] = nums[i]

        self.exec(0, n-1, nums, dp)
        return True if dp[0][n-1] >= sum(nums)/2 else False

    def exec(self, left: int, right: int, nums: List[int], dp: List[List[int]]):
        if dp[left][right] >= 0:
            return

        self.exec(left+1, right, nums, dp)
        self.exec(left, right-1, nums, dp)

        dp[left][right] = sum(nums[left:right+1]) - min(dp[left+1][right], dp[left][right-1])
