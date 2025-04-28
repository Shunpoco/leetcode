class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        result = 0
        total = 0

        idx = 0
        for j in range(len(nums)):
            total += nums[j]
            while idx <= j and total * (j - idx + 1) >= k:
                total -= nums[idx]
                idx += 1

            result += j - idx + 1

        return result
