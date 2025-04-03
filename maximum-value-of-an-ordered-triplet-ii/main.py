class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)

        lm = [0] * n
        rm = [0] * n

        for i in range(1, n):
            lm[i] = max(lm[i-1], nums[i-1])
            rm[n-1-i] = max(rm[n-i], nums[n-i])

        result = 0
        for i in range(1, n-1):
            result = max(result, (lm[i]-nums[i])*rm[i])

        return result

