class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        memo = defaultdict(bool)

        result = -1
        for num in nums:
            memo[num] = True

            if memo[-1*num] and result < abs(num):
                result = abs(num)

        return result

