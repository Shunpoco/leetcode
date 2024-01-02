class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        result = []

        pos = 0
        for i, num in enumerate(nums):
            if i == 0 or num != nums[i-1]:
                pos = 0
            else:
                pos += 1

            if pos == len(result):
                result.append([])

            result[pos].append(num)

        return result
