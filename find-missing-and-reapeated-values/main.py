class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)

        memo = [0 for _ in range(n*n+1)]

        for i in range(n):
            for j in range(n):
                memo[grid[i][j]] += 1

        result = [0, 0]
        for i, v in enumerate(memo):
            if v == 0:
                result[1] = i
            elif v == 2:
                result[0] = i

        return result

