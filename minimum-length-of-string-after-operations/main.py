class Solution:
    def minimumLength(self, s: str) -> int:
        memo = defaultdict(int)

        for c in s:
            memo[c] += 1

        result = 0
        for _, n in memo.items():
            if n % 2 == 0:
                result += 2
            else:
                result += 1

        return result

