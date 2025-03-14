class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        max_candies = max(candies)

        l, r = 0, max_candies

        while l < r:
            m = (l+r+1) // 2

            if self.calc(candies, k, m):
                l = m
            else:
                r = m - 1

        return l

    def calc(self, candies, k, num):
        max_children = 0

        for c in candies:
            max_children += c // num

        return max_children >= k
        
