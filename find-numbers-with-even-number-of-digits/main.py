class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        result = 0

        for num in nums:
            t = 0
            while num > 0:
                t += 1
                num //= 10

            result += 1 if t % 2 == 0 else 0

        return result
