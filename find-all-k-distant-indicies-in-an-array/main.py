class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        keys = []
        for i, num in enumerate(nums):
            if num == key:
                keys.append(i)

        result = []
        for i in range(len(nums)):
            v = min([abs(x-i) for x in keys])
            if v <= k:
                result.append(i)

        return result

