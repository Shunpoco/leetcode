class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        r = 0
        for i in range(2**len(nums)):
            t = 0
            for j in range(len(nums)):
                if i & 2**j > 0:
                    t ^= nums[j]

            r += t

        return r
