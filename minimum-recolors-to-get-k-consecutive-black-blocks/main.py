class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        result = float('inf')

        for i in range(len(blocks)-k+1):
            v = self.count(blocks[i:i+k])

            if result > v:
                result = v

        return result

    def count(self, s):
        count = 0

        for c in s:
            if c == 'W':
                count += 1

        return count

