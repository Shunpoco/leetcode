class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        sums = sum(nums)

        t = sum(nums[:sums])
        if t == sums:
            return 0

        result = sums - t
        for i in range(1, len(nums)):
            t -= nums[i-1]
            t += nums[(sums+i-1)%len(nums)]

            result = min(result, sums-t)

        return result
