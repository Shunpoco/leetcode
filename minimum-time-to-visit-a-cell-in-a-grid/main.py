class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1

        row, col = len(grid), len(grid[0])

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = set()

        pq = [(grid[0][0], 0, 0)]

        while len(pq) > 0:
            ct, i, j = heapq.heappop(pq)

            if (i, j) == (row-1, col-1):
                return ct

            if (i, j) in visited:
                continue

            visited.add((i, j))

            for dx, dy in directions:
                nr, nc = i + dx, j + dy

                if not self.valid(visited, nr, nc, row, col):
                    continue

                wt = (1 if (grid[nr][nc] - ct) % 2 == 0 else 0)

                nt = max(grid[nr][nc] + wt, ct + 1)

                heapq.heappush(pq, (nt, nr, nc))

        return -1

    def valid(self, visited, i, j, row, col):
        return 0 <= i < row and 0 <= j < col and (i, j) not in visited
