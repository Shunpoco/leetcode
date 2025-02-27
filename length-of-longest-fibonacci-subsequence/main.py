class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        result = 0

        dp = [[0 for _ in range(len(arr))] for _ in range(len(arr))]

        memo = {value: idx for idx, value in enumerate(arr)}

        for cur in range(len(arr)):
            for prev in range(cur):
                diff = arr[cur] - arr[prev]
                pi = memo.get(diff, -1)

                dp[prev][cur] = dp[pi][prev] + 1 if diff < arr[prev] and pi >= 0 else 2

                result = max(result, dp[prev][cur])

        return result if result >= 3 else 0

