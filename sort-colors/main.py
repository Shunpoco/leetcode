class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        memo = {}
        memo[0] = 0
        memo[1] = 0
        memo[2] = 0
        for num in nums:
            memo[num] += 1

        i = 0
        for j in range(3):
            for _ in range(memo[j]):
                nums[i] = j
                i += 1

