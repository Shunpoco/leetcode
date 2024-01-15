class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        memo = defaultdict(int)

        for match in matches:
            if memo.get(match[0]) is None:
                memo[match[0]] = 0

            memo[match[1]] -= 1

        zero, one = [], []
        for p, l in memo.items():
            if l == 0:
                zero.append(p)
            elif l == -1:
                one.append(p)

        zero.sort()
        one.sort()

        return [zero, one]
