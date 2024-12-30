class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        memo = [[-1 for _ in range(len(target))] for _ in range(len(words[0]))]
        count_c = [[0 for _ in range(26)] for _ in range(len(words[0]))]
        for i in range(len(words)):
            for j in range(len(words[0])):
                c = ord(words[i][j]) - ord('a')
                count_c[j][c] += 1

        return self.dp(words, target, 0, 0, memo, count_c)

    def dp(self, words, target, i, j, memo, count_c):
        if j == len(target):
            return 1

        if i == len(words[0]) or len(words[0]) - i < len(target) - j:
            return 0

        if memo[i][j] != -1:
            return memo[i][j]

        count = 0

        cur = ord(target[j]) - ord('a')

        count += self.dp(words, target, i+1, j, memo, count_c)
        count += count_c[i][cur] * self.dp(words, target, i+1, j+1, memo, count_c)

        memo[i][j] = count % 1000000007

        return memo[i][j]
