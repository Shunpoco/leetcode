class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = heights.copy()

        expected.sort()

        r = 0
        for a, b in zip(heights, expected):
            if a != b:
                r += 1

        return r

