from typing import List

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        memo = {}
        for i in range(1, n+1):
            memo[i] = 0

        for a, b in trust:
            memo[b] += 1
            memo[a] -= 1

        for k, v in memo.items():
            if v == n-1:
                return k

        return -1
