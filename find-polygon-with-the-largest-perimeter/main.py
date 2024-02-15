class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()

        s = sum(nums)

        for i in range(len(nums)-1, 1, -1):
            if nums[i] < s - nums[i]:
                return s

            s -= nums[i]

        return -1
