class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        result = 0

        for i in range(len(nums)):
            diff = abs(nums[i] - nums[(i+1)%len(nums)])
            if diff > result:
                print(result, diff)
                result = diff

        return result
