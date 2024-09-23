class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        memo = defaultdict(list)

        for word in dictionary:
            memo[word[0]].append(word)

        dp = [-1 for _ in range(len(s)+1)]

        self.calc(s, 0, memo, dp)

        return dp[0]

    def calc(self, s, idx, memo, dp):
        if idx >= len(s):
            dp[idx] = 0
            return

        if dp[idx] != -1:
            return

        self.calc(s, idx+1, memo, dp)
        result = 1 + dp[idx+1]

        for word in memo[s[idx]]:
            if s[idx:idx+len(word)] == word:
                self.calc(s, idx+len(word), memo, dp)
                t = dp[idx+len(word)]
                if t < result:
                    result = t

        dp[idx] = result

        return
