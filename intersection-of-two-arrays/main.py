class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        memo = {}

        for num in nums1:
            memo[num] = True

        result = []

        for num in nums2:
            if memo.get(num, False):
                result.append(num)
                memo[num] = False

        return result

