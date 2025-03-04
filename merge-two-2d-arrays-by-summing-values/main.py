class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        result = []

        n1, n2 = len(nums1), len(nums2)

        i, j = 0, 0

        while i < n1 and j < n2:
            v1, v2 = nums1[i], nums2[j]

            if v1[0] == v2[0]:
                result.append([v1[0], v1[1]+v2[1]])
                i += 1
                j += 1
            elif v1[0] < v2[0]:
                result.append(v1)
                i += 1
            else:
                result.append(v2)
                j += 1

        while i < n1:
            result.append(nums1[i])
            i += 1

        while j < n2:
            result.append(nums2[j])
            j += 1

        return result

