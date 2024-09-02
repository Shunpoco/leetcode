class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        s = sum(chalk)
        k %= s

        t = 0
        for i, c in enumerate(chalk):
            t += c
            if t > k:
                return i

        return -1
