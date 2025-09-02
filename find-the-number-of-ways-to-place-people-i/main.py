class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        result = 0
        n = len(points)

        for i in range(n):
            pa = points[i]
            for j in range(n):
                pb = points[j]

                if i == j or not (pa[0] <= pb[0] and pa[1] >= pb[1]):
                    continue

                if n == 2:
                    result += 1
                    continue

                illegal = False
                for k in range(n):
                    if k == i or k == j:
                        continue

                    t = points[k]
                    xc = t[0] >= pa[0] and t[0] <= pb[0]
                    yc = t[1] <= pa[1] and t[1] >= pb[1]

                    if xc and yc:
                        illegal = True
                        break

                if not illegal:
                    result += 1

        return result

