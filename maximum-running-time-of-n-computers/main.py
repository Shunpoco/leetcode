from typing import Lilst

class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        batteries.sort()
        l = len(batteries)
        live = [0 for _ in range(n)]
        for i in range(n):
            live[n-1-i] = batteries[l-1-i]
            batteries[l-1-i] = 0

        extra = sum(batteries)

        result = live[0]
        for i in range(n-1):
            diff = live[i+1] - live[i]

            if extra >= diff * (i+1):
                extra -= diff * (i+1)
                result = live[i+1]
            elif extra >= i+1:
                result += extra // (i+1)
                extra -= extra // (i+1) * (i+1)
                break
            else:
                break

        if extra >= n:
            result += extra // n

        return result

