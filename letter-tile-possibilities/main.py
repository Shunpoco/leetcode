class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        saw = set()

        tiles = "".join(sorted(tiles))

        return self.calc(tiles, "", 0, saw)-1


    def factorial(self, n):
        if n <= 1:
            return 1

        result = 1
        for num in range(2, n+1):
            result *= num

        return result

    def permutations(self, s):
        result = self.factorial(len(s))

        for c in Counter(s).values():
            result //= self.factorial(c)

        return result

    def calc(self, tiles, cur, pos, saw):
        if pos >= len(tiles):
            if cur not in saw:
                saw.add(cur)
                
                return self.permutations(cur)

            return 0

        return self.calc(tiles, cur, pos+1, saw) + self.calc(tiles, cur+tiles[pos], pos+1, saw)
