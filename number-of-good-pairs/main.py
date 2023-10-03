class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        memo = defaultdict(list)

        result = 0
        for i, num in enumerate(nums):
            memo[num].append(i)

            if len(memo[num]) > 1:
                result += len(memo[num]) - 1

        return result

