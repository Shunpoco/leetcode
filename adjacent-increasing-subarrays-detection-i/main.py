class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        for i in range(len(nums)-2*k+1):
            if self.ok(nums[i:i+2*k]):
                return True

        return False



    def ok(self, nums: List[int]) -> bool:
        m = len(nums) // 2
        
        for i in range(1, m):
            if nums[i] <= nums[i-1]:
                return False

        for i in range(m+1, len(nums)):
            if nums[i] <= nums[i-1]:
                return False

        return True

