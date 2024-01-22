class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)

        memo = [0 for _ in range(n)]

        dup = -1
        for num in nums:
            memo[num-1] += 1
            if memo[num-1] == 2:
                dup = num

        no = memo.index(0) + 1

        return [dup, no]
