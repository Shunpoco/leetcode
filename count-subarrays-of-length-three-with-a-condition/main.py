class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        result = 0
        
        for i in range(len(nums)-2):
            first, second, third = nums[i], nums[i+1], nums[i+2]

            if 2*(first+third) == second:
                result += 1

        return result

