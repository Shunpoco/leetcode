class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        n = len(values)

        l = values[0]

        result = 0

        for i in range(1, n):
            r = values[i] - i
            result = max(result, l + r)

            c = values[i] + i

            l = max(l, c)

        return result
