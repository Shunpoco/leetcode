class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n = len(nums)

        r = 0
        for i in range(2**n):
            t = 0
            for j in range(n):
                if i & 2**j > 0:
                    t ^= nums[j]

            r += t

        return r

