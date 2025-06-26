class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        sums = 0
        count = 0
        bits = k.bit_length()

        for i, ch in enumerate(s[::-1]):
            if ch == '1':
                if i < bits and sums + (1 << i) <= k:
                    sums += 1 << i
                    count += 1
            else:
                count += 1

        return count
