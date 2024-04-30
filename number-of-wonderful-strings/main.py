class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        ia = ord('a')
        count = defaultdict(int)

        count[0] = 1
        result = 0
        bm = 0

        for c in word:
            i = ord(c) - ia
            bm ^= 1 << i
            result += count[bm]

            for j in range(10):
                result += count[bm ^ (1 << j)]

            count[bm] += 1

        return result

