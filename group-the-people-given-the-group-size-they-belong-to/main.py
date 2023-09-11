from collections import defaultdict
from typing import List

class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        d = defaultdict(list)

        for i, c in enumerate(groupSizes):
            if len(d[c]) > 0 and len(d[c][-1]) < c:
                d[c][-1].append(i)
            else:
                d[c].append([i])


        result = []
        for _, v in d.items():
            result.extend(v)

        return result

