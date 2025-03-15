class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        mins, maxs = 1, max(nums)

        while mins < maxs:
            m = (mins + maxs) // 2
            p = 0

            i = 0
            while i < len(nums):
                if nums[i] <= m:
                    p += 1
                    i += 2
                else:
                    i += 1

            if p >= k:
                maxs = m
            else:
                mins = m + 1

        return mins
