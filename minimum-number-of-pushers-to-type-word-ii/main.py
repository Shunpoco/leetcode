class Solution:
    def minimumPushes(self, word: str) -> int:
        char_count = defaultdict(int)
        for c in word:
            char_count[c] += 1

        vals = list(char_count.values())
        vals.sort()
        vals.reverse()

        result = 0
        for i, val in enumerate(vals):
            result += val * (i//8+1)

        return result
