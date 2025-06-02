class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)

        result = n

        left = [0] * n
        for i in range(1, n):
            t = left[i-1]
            if ratings[i] > ratings[i-1]:
                left[i] = t + 1

        right = [0] * n
        for i in range(n-2, -1, -1):
            t = right[i+1]
            if ratings[i] > ratings[i+1]:
                right[i] = t + 1

        for i in range(n):
            result += max(left[i], right[i])

        return result

