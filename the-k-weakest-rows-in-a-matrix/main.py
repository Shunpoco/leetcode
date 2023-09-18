class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        r = []

        for i, m in enumerate(mat):
            v = sum(m)
            r.append((v, i))

        r.sort()

        result = [r[i][1] for i in range(k)]

        return result

