from typing import List

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        dp = [-1 for _ in range(len(s)+1)]
        dp[len(s)] = 0

        def exec(idx: int):
            if dp[idx] != -1:
                return

            r = 100000
            for start in range(idx, len(s)):
                for end in range(len(s), start, -1):
                    pref = start - idx
                    v = s[start:end]

                    if v in dictionary:
                        exec(end)
                        if pref + dp[end] < r:
                            r = pref + dp[end]

                    else:
                        exec(end)
                        t = end - start + dp[end]
                        if pref + t < r:
                            r = pref + t

            dp[idx] = r

        exec(0)

        return dp[0]

