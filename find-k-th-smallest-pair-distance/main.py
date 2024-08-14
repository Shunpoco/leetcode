class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        length = len(nums)

        low = 0
        high = nums[length - 1] - nums[0]

        while low < high:
            mid = (low + high) // 2

            count = self.count_pairs(nums, mid)

            if count < k:
                low = mid + 1
            else:
                high = mid

        return low

    def count_pairs(self, nums, maxd) -> int:
        count = 0
        length = len(nums)
        l = 0

        for r in range(length):
            while nums[r] - nums[l] > maxd:
                l += 1

            count += r - l

        return count
