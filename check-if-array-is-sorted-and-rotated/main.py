class Solution:
    def check(self, nums: List[int]) -> bool:
        s = nums.copy()
        s.sort()

        for i in range(len(nums)):
            nums = nums[1:] + nums[:1]

            if nums == s:
                return True

        return False

