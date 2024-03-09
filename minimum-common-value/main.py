class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        memo = defaultdict(bool)

        for num in nums1:
            memo[num] = True

        for num in nums2:
            if memo[num]:
                return num

        return -1
