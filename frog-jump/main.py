from typing import List

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if stones[1] != 1:
            return False

        memo = {}

        def calc(idx: int, unit: int):
            if idx == len(stones)-1:
                memo[(idx, unit)] = True
                return
            if memo.get((idx, unit)) is not None:
                return

            p = stones[idx]
            result = False
            for j in range(idx+1, len(stones)):
                v = stones[j]
                if v in [p+unit-1, p+unit, p+unit+1]:
                    calc(j, v-p)
                    result |= memo[(j, v-p)]
                    if result:
                        break
                elif v > p+unit+1:
                    break

            memo[(idx, unit)] = result    

        calc(1, 1)

        return memo[(1, 1)]

