class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums.sort()

        result = 0
        l, r = 0, 1

        while r < len(nums):
            if nums[r] - nums[l] == 1:
                r += 1
                if r - l > result:
                    result = r - l
            elif nums[r] - nums[l] == 0:
                r += 1
            else:
                l += 1

        return result
