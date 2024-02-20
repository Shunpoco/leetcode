class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s = sum([i for i in range(len(nums)+1)])

        return s - sum(nums)
