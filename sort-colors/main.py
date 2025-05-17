class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        memo = [0] * 3

        for num in nums:
            memo[num] += 1

        idx = 0
        for i in range(3):
            while memo[i] > 0:
                nums[idx] = i
                memo[i] -= 1
                idx += 1

