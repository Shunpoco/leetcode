class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)

        count, pre, result = 1, 0, 0
        for i in range(1, n):
            if nums[i] > nums[i-1]:
                count += 1
            else:
                pre, count = count, 1
            result = max(result, min(pre, count))
            result = max(result, count // 2)

        return result

