class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        result = [[-1 for _ in range(len(isWater[0]))] for _ in range(len(isWater))]

        q = []
        for i in range(len(isWater)):
            for j in range(len(isWater[0])):
                if isWater[i][j] == 1:
                    result[i][j] = 0
                    q.append((i, j, 0))

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while len(q) > 0:
            i, j, height = q.pop(0)

            for d in directions:
                ni, nj = i + d[0], j + d[1]

                if ni < 0 or ni >= len(isWater) or nj < 0 or nj >= len(isWater[0]) or result[ni][nj] != -1:
                    continue

                result[ni][nj] = height + 1
                q.append((ni, nj, height+1))

        return result

