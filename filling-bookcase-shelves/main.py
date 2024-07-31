class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        memo = [[0 for _ in range(shelfWidth+1)] for _ in range(len(books))]

        return self.f(books, shelfWidth, 0, shelfWidth, 0, memo)


    def f(self, books, shelfWidth, i, remain, maxHeight, memo) -> int:
        cur = books[i]

        newMax = max(maxHeight, cur[1])
        if i == len(books)-1:
            if remain >= cur[0]:
                return newMax
            return maxHeight + cur[1]

        if memo[i][remain] != 0:
            return memo[i][remain]

        # new shelf
        height = maxHeight + self.f(books, shelfWidth, i+1, shelfWidth-cur[0], cur[1], memo)

        if remain >= cur[0]:
            height2 = self.f(books, shelfWidth, i+1, remain-cur[0], newMax, memo)
            height = min(height, height2)

        memo[i][remain] = height

        return height
