class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        return self.calc(rectangles, 0) or self.calc(rectangles, 1)

    def calc(self, rectangles, dim):
        gaps = 0

        rectangles.sort(key=lambda x: x[dim])
        end = rectangles[0][dim+2]

        for i in range(1, len(rectangles)):
            r = rectangles[i]

            if end <= r[dim]:
                gaps += 1

            end = max(end, r[dim+2])

        return gaps >= 2
