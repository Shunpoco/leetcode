class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        h1 = {}
        h2 = {}

        for num in nums1:
            if h1.get(num) is None:
                h1[num] = 1
            else:
                h1[num] += 1

        for num in nums2:
            if h2.get(num) is None:
                h2[num] = 1
            else:
                h2[num] += 1

        unique = set(nums1).intersection(set(nums2))
        r = []
        for u in unique:
            i = min(h1[u], h2[u])
            for _ in range(0, i):
                r.append(u)

        return r
