from typing import List, Dict

class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        m = len(req_skills)
        n = len(people)
        memo = {}
        for i, skill in enumerate(req_skills):
            memo[skill] = pow(2, i)

        dp = [[[-1] for _ in range(pow(2, m))] for _ in range(n)]

        self.exec(0, 0, dp, memo, people)

        return dp[0][0]

    def exec(self, p: int, s: int, dp: List[List[List[int]]], reqs: Dict[str, int], people: List[List[str]]):
        if len(dp[p][s]) == 0 or dp[p][s][0] >= 0:
            return

        result = []
        # Case 1: Choose the people p
        peo = people[p]
        t = s
        for skill in peo:
            t |= reqs.get(skill, 0)
        result = [p]
        if p == len(people) - 1:
            if t != len(dp[0]) - 1:
                result = []
        elif t != len(dp[0]) - 1:
                self.exec(p+1, t, dp, reqs, people)
                if len(dp[p+1][t]) > 0:
                    result.extend(dp[p+1][t])
                else:
                    result = []

        # Case 2: Doesn't choose the poeple p
        if p < len(people)-1:
            self.exec(p+1, s, dp, reqs, people)
            t = dp[p+1][s]

            if len(t) > 0 and (len(result) == 0 or len(result) > len(t)):
                result = t

        dp[p][s] = result.copy()

        return
