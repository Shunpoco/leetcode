class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        result = []

        n = len(mat)
        m = len(mat[0])

        for d in range(n+m-1):
            t = []

            r = 0 if d < m else d - m + 1
            c = d if d < m else m -1

            while r < n and c > -1:
                t.append(mat[r][c])
                r += 1
                c -= 1

            if d % 2 == 0:
                result.extend(t[::-1])
            else:
                result.extend(t)

        return result

