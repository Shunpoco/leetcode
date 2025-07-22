
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        cums = [0] * (n+1)

        t = 0
        for i, num in enumerate(nums):
            t += num
            cums[i+1] = t

        memory = {}
        result = 0
        left = 0

        for right in range(n):
            if memory.get(nums[right]) is not None and memory[nums[right]] >= left:
                left = memory[nums[right]] + 1

            memory[nums[right]] = right
            s = cums[right+1] - cums[left]

            if s > result:
                result = s

        return result

