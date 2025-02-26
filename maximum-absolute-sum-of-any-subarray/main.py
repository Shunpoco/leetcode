class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        min_sum = float('inf')
        max_sum = float('-inf')

        prefix_sum = 0
        max_abs = 0

        for num in nums:
            prefix_sum += num

            min_sum = min(min_sum, prefix_sum)
            max_sum = max(max_sum, prefix_sum)

            if prefix_sum >= 0:
                max_abs = max(max_abs, max(prefix_sum, prefix_sum - min_sum))

            elif prefix_sum <= 0:
                max_abs = max(max_abs, max(abs(prefix_sum), abs(prefix_sum - max_sum)))

        return max_abs
