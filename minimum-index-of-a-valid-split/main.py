class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        memo1 = defaultdict(int)
        memo2 = defaultdict(int)

        n = len(nums)

        for num in nums:
            memo2[num] += 1

        for i in range(n):
            num = nums[i]
            memo2[num] -= 1
            memo1[num] += 1

            if memo1[num] * 2 > i + 1 and memo2[num] * 2 > n - i - 1:
                return i

        return -1

