class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1 for _ in range(n)]

        left, right = 1, 1

        for i in range(n):
            result[i] *= left
            result[n-1-i] *= right
            left *= nums[i]
            right *= nums[n-1-i]

        return result

