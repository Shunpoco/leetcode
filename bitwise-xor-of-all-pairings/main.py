class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        m1 = len(nums1) % 2
        m2 = len(nums2) % 2

        if m1 == 0 and m2 == 0:
            return 0

        if m1 == 0:
            result = 0
            for n in nums1:
                result ^= n

            return result

        if m2 == 0:
            result = 0
            for n in nums2:
                result ^= n
            
            return result

        result = 0
        for n in nums1:
            result ^= n

        for n in nums2:
            result ^= n

        return result

