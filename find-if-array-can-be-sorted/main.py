class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        same_set_bits = []

        start = 0
        end = 1

        while end < len(nums):
            if nums[start].bit_count() == nums[end].bit_count():
                end += 1
            else:
                same_set_bits.append((start, end))
                start = end
                end = start + 1

        same_set_bits.append((start, end))

        flipped_nums = []
        for start, end in same_set_bits:
            t = nums[start:end]
            t.sort()
            flipped_nums.extend(t)

        nums.sort()

        return flipped_nums == nums

