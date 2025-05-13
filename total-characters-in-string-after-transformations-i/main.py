class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        MOD = 10 ** 9 + 7

        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1

        for _ in range(t):
            temp = [0] * 26
            temp[0] = count[25]
            temp[1] = (count[25] + count[0]) % MOD

            for i in range(2, 26):
                temp[i] = count[i-1]

            count = temp

        return sum(count) % MOD
