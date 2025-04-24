class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        result = 0

        memo = {}
        n = len(nums)
        r = 0
        sets = len(set(nums))

        for l in range(n):
            if l > 0:
                remove = nums[l-1]
                memo[remove] -= 1
                if memo[remove] == 0:
                    memo.pop(remove)

            while r < n and len(memo) < sets:
                add = nums[r]
                memo[add] = memo.get(add, 0) + 1
                r += 1
            if len(memo) == sets:
                result += n - r + 1

        return result

