class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()

        result = 0

        for i in range(len(nums)):
            low = self.search_bound(nums, i+1, len(nums)-1, lower-nums[i])
            high =self.search_bound(nums, i+1, len(nums)-1, upper-nums[i]+1)

            result += high - low

        return result


    def search_bound(self, nums, low, high, target):
        while low <= high:
            mid = low + ((high-low) // 2)

            if nums[mid] >= target:
                high = mid - 1
            else:
                low = mid + 1

        return low
