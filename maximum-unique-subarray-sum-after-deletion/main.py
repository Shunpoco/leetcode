
class Solution:
    def maxSum(self, nums: List[int]) -> int:
        nums = list(set(nums))
        nums.sort(reverse=True)

        result = nums[0]

        for i in range(1, len(nums)):
            if nums[i] > 0:
                result += nums[i]

        return result

