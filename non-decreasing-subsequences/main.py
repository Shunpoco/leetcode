from collections import defaultdict
from typing import List

class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        result = defaultdict(bool)
        n = len(nums)
        for i in range(n):
            self.execute(i, [nums[i]], result, nums)

        return list(result.keys())

    def execute(self, idx: int, arr: List[int], result: Dict, nums: List[int]):
        if idx == len(nums):
            return

        for i in range(idx+1, len(nums)):
            if nums[i] >= arr[-1]:
                arr.append(nums[i])
                if result.get(tuple(arr)) is None:
                    result[tuple(arr)] = True
                    self.execute(i, arr, result, nums)
                arr.pop(-1)

        return
