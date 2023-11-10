from typing import List

class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        memo = defaultdict(list)
        for a in adjacentPairs:
            memo[a[0]].append(a[1])
            memo[a[1]].append(a[0])

        for k, v in memo.items():
            if len(v) == 1:
                m = k
                break

        result = [m]
        while len(result) < len(adjacentPairs)+1:
            nex = memo[result[-1]]
            if len(nex) == 1:
                result.append(nex[0])
            else:
                if nex[0] == result[-2]:
                    result.append(nex[1])
                else:
                    result.append(nex[0])

        return result

