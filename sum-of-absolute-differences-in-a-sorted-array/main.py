class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        sums = [0 for _ in range(n)]

        t = 0
        for i, num in enumerate(nums):
            t += num
            sums[i] = t

        result = [0 for _ in range(n)]
        for i in range(n):
            v = nums[i]
            left = 0 if i == 0 else sums[i-1]
            right = 0 if i == n - 1 else sums[-1]

            lr = 0 if left == 0 else v * i - left
            rr = 0 if right == 0 else (right - sums[i]) - v * (n-i-1)

            result[i] = lr + rr

        return result
