class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [-1 for _ in range(target+1)]

        self.exec(0, nums, target, dp)

        return dp[0]

    def exec(self, s, nums, t, dp):
        if dp[s] != -1:
            return

        if s == t:
            dp[s] = 1
            return

        r = 0
        for num in nums:
            if s + num <= t:
                self.exec(s+num, nums, t, dp)
                r += dp[s+num]


        dp[s] = r

        return
