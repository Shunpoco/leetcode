class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0

        result = []
        t = 0
        for num in nums:
            if num != 0:
                result.append(num)
            else:
                t += 1

        for _ in range(t):
            result.append(0)

        return result

