class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        n = len(nums1)

        l, r = -(10**10), 10**10

        while l <= r:
            mid = (l + r) // 2
            count = 0

            for i in range(n):
                count += self.calc(nums2, nums1[i], mid)
            
            if count < k:
                l = mid + 1
            else:
                r = mid - 1

        return l

    def calc(self, nums2, x1, v):
        if x1 > 0:
            return bisect_right(nums2, v // x1)
        elif x1 < 0:
            return len(nums2) - bisect_left(nums2, -(-v // x1))

        return len(nums2) if v >= 0 else 0

