class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        memo = defaultdict(int)

        for num in nums:
            memo[num] += 1
            if memo[num] == 2:
                memo[num] = 0

        for _, val in memo.items():
            if val != 0:
                return False

        return True

