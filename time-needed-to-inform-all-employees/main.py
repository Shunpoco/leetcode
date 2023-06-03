from typing import List

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        subordinates = [[] for _ in range(n)]
        for e, m in enumerate(manager):
            if m >= 0:
                subordinates[m].append(e)

        result = 0
        queue = [(headID, 0)]

        while len(queue) > 0:
            e, t = queue.pop(0)

            if t > result:
                result = t

            t += informTime[e]

            for subordinate in subordinates[e]:
                queue.append((subordinate, t))

        return result

