class Solution:
    def minDifference(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 4:
            return 0

        nums.sort()

        diff = float("inf")

        for l in range(4):
            r = n - 4 + l
            diff = min(diff, nums[r]-nums[l])

        return diff

