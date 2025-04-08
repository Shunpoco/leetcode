class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        memo = defaultdict(int)

        for num in nums:
            memo[num] += 1

        result = 0
        while self.isDup(memo):
            result += 1
            for i in range(min(3, len(nums))):
                memo[nums[i]] -= 1
            
            nums = nums[3:]

        return result

    def isDup(self, memo) -> bool:
        for _, v in memo.items():
            if v > 1:
                return True

        return False

