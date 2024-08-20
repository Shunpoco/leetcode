class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        memo = [[0 for _ in range(len(piles))] for _ in range(len(piles))]

        suffs = piles.copy()

        for i in range(len(suffs)-2, -1, -1):
            suffs[i] += suffs[i+1]

        return self.calc(suffs, 0, 1, memo)

    def calc(self, suffs, idx, m, memo):
        if idx + 2 * m >= len(suffs):
            return suffs[idx]

        if memo[idx][m] > 0:
            return memo[idx][m]

        result = float('inf')

        for i in range(1, 2*m+1):
            result = min(result, self.calc(suffs, idx+i, max(i, m), memo))

        memo[idx][m] = suffs[idx] - result

        return memo[idx][m]
