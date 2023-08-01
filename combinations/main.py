from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []

        def choose(cur: List[int]):
            if len(cur) == k:
                result.append(cur)
                return

            c = cur[-1] if len(cur) > 0 else 0

            if len(cur) + (n-c) < k:
                return

            for i in range(c+1, n+1):
                t = cur.copy()
                t.append(i)
                choose(t)

        choose([])

        return result
