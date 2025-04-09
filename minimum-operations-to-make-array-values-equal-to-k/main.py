class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        memo = set()

        for num in nums:
            if num < k:
                return -1
            if num > k:
                memo.add(num)

        return len(memo)
