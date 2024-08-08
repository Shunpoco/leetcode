class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        ds = [(0,1), (1,0), (0,-1), (-1,0)]

        result = []
        s = 1
        d = 0

        while len(result) < rows * cols:
            for _ in range(2):
                for _ in range(s):
                    if rStart >= 0 and rStart < rows and cStart >= 0 and cStart < cols:
                        result.append([rStart, cStart])

                    rStart += ds[d][0]
                    cStart += ds[d][1]

                d = (d + 1) % 4
            s += 1

        return result
