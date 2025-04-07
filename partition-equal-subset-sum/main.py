class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False

        target = total // 2

        dp = [False for _ in range(target+1)]
        dp[0] = True

        for num in nums:
            for cur in range(target, num-1, -1):
                dp[cur] = dp[cur] or dp[cur-num]

        return dp[target]

