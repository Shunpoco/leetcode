class Cell:
    def __init__(self, height, row, col):
        self.height = height
        self.row = row
        self.col = col

    def __lt__(self, other):
        return self.height < other.height

class Solution:
    def validCell(self, row, col, n_rows, n_cols):
        return 0 <= row < n_rows and 0 <= col < n_cols

    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        d_row = [0, 0, -1, 1]
        d_col = [-1, 1, 0, 0]

        n_rows = len(heightMap)
        n_cols = len(heightMap[0])

        visited = [[False for _ in range(n_cols)] for _ in range(n_rows)]

        boundary = []

        for i in range(n_rows):
            heapq.heappush(boundary, Cell(heightMap[i][0], i, 0))
            heapq.heappush(boundary, Cell(heightMap[i][n_cols-1], i, n_cols-1))
            visited[i][0] = True
            visited[i][n_cols-1] = True

        for i in range(n_cols):
            heapq.heappush(boundary, Cell(heightMap[0][i], 0, i))
            heapq.heappush(boundary, Cell(heightMap[n_rows-1][i], n_rows-1, i))
            visited[0][i] = True
            visited[n_rows-1][i] = True

        result = 0
        while boundary:
            cur = heapq.heappop(boundary)

            cur_row = cur.row
            cur_col = cur.col
            min_height = cur.height

            for d in range(4):
                tr = cur_row + d_row[d]
                tc = cur_col + d_col[d]

                if self.validCell(tr, tc, n_rows, n_cols) and not visited[tr][tc]:
                    t = heightMap[tr][tc]

                    if t < min_height:
                        result += min_height - t

                    heapq.heappush(boundary, Cell(max(t, min_height), tr, tc))
                    visited[tr][tc] = True

        return result

