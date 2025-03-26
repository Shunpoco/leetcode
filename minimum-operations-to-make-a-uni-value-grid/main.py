class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        result = 0
        nums = []

        for row in grid:
            for v in row:
                nums.append(v)

        nums.sort()
        l = len(nums)

        common = nums[l // 2]

        for n in nums:
            if n % x != common % x:
                return -1
            result += abs(common-n) // x

        return result

