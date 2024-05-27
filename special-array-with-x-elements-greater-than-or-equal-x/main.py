class Solution:
    def specialArray(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()

        r = -1
        for i in range(n):
            if nums[n-1-i] >= i+1 and (i == n-1 or nums[n-1-i-1] < i+1):
                r = i + 1

        return r

