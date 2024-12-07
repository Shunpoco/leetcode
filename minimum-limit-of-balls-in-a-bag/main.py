class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        l, r = 1, max(nums)

        while l < r:
            m = (l+r) // 2

            if self.is_possible(m, nums, maxOperations):
                r = m
            else:
                l = m + 1

        return l

    def is_possible(self, m, nums, mo):
        total = 0

        for num in nums:
            op = math.ceil(num / m) - 1
            total += op

            if total > mo:
                return False

        return True

