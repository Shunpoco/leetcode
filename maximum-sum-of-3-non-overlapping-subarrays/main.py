class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n = len(nums) - k + 1

        sums = [sum(nums[:k])]
        for i in range(k, len(nums)):
            sums.append(sums[-1]-nums[i-k]+nums[i])

        memo = [[-1 for _ in range(4)] for _ in range(n)]
        result = []

        self.dp(sums, k, 0, 3, memo)
        self.dfs(sums, k, 0, 3, memo, result)

        return result

    def dp(self, sums, k, idx, rem, memo):
        if rem == 0:
            return 0

        if idx >= len(sums):
            return float("-inf") if rem > 0 else 0

        if memo[idx][rem] != -1:
            return memo[idx][rem]

        w_cur = sums[idx] + self.dp(sums, k, idx+k, rem-1, memo)
        wo_cur = self.dp(sums, k, idx+1, rem, memo)

        memo[idx][rem] = max(w_cur, wo_cur)

        return memo[idx][rem]

    def dfs(self, sums, k, idx, rem, memo, result):
        if rem == 0 or idx >= len(sums):
            return

        w_cur = sums[idx] + self.dp(sums, k, idx+k, rem-1, memo)
        wo_cur = self.dp(sums, k, idx+1, rem, memo)

        if w_cur >= wo_cur:
            result.append(idx)
            self.dfs(sums, k, idx+k, rem-1, memo, result)
        else:
            self.dfs(sums, k, idx+1, rem, memo, result)

