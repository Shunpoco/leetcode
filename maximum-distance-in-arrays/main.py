class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        s = arrays[0][0]
        m = arrays[0][-1]
        md = 0

        for i in range(1, len(arrays)):
            ar = arrays[i]

            md = max(md, abs(ar[-1]-s), abs(ar[0]-m))
            s = min(s, ar[0])
            m = max(m, ar[-1])

        return md
