class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return self.bs(nums, 0, len(nums)-1, target)

    def bs(self, nums: List[int], start: int, end: int, target: int) -> int:
        m = (start+end) // 2

        if nums[m] == target:
            return m

        if start == end:
            if nums[start] < target:
                return start + 1
            else:
                return start

        if nums[m] < target:
            return self.bs(nums, m+1, end, target)
        else:
            return self.bs(nums, start, m, target)

        
