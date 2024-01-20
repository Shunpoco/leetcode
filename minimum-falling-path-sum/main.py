class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)

        dp = matrix[n-1].copy()

        for row in range(n-2, -1, -1):
            t = [0 for _ in range(n)]
            for col in range(n):
                t[col] = matrix[row][col]
                b = [dp[col]]
                if col > 0:
                    b.append(dp[col-1])
                if col < n-1:
                    b.append(dp[col+1])
                
                t[col] += min(b)

            dp = t

        return min(dp)
