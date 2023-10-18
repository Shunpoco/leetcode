from typing import List

class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        depends = [[] for _ in range(n)]
        for relation in relations:
            depends[relation[1]-1].append(relation[0]-1)

        takes = [-1 for _ in range(n)]

        def calc(idx: int):
            if takes[idx] >= 0:
                return
            
            v = time[idx]

            for d in depends[idx]:
                calc(d)
                t = time[idx] + takes[d]
                if t > v:
                    v = t

            takes[idx] = v

        for i in range(n):
            calc(i)

        return max(takes)

