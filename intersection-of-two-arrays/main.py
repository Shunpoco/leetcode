class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = [0 for _ in range(1001)]

        for num in nums1:
            n[num] = 1

        res = {}
        for num in nums2:
            if n[num] == 1:
                res[num] = True

        return list(res.keys())
