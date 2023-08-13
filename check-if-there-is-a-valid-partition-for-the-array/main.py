from typing import List, Dict

class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        memo = {}

        self.calc(0, n, nums, memo)

        return memo[0]

    def calc(self, idx: int, n: int, nums: List[int], memo: Dict[int, bool]):
        if memo.get(idx) is not None:
            return

        if idx == n:
            memo[n] = True
            return

        result = False

        if idx+1 < n and nums[idx] == nums[idx+1]:
            self.calc(idx+2, n, nums, memo)
            result |= memo[idx+2]

        if idx+2 < n and nums[idx] == nums[idx+1] and nums[idx+1] == nums[idx+2]:
            self.calc(idx+3, n, nums, memo)
            result |= memo[idx+3]

        if idx+2 < n and nums[idx]+1 == nums[idx+1] and nums[idx+1]+1 == nums[idx+2]:
            self.calc(idx+3, n, nums, memo)
            result |= memo[idx+3]

        memo[idx] = result

