class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        bits = 0
        l = 0
        result = 0

        for r in range(len(nums)):
            while bits & nums[r] != 0:
                bits ^= nums[l]
                l += 1

            bits |= nums[r]

            result = max(result, r-l+1)

        return result

