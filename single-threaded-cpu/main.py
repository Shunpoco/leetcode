from typing import List

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        q = []
        r = []
        tasks = [(v[0], v[1], idx) for idx, v in enumerate(tasks)]
        tasks.sort()
        t = 0
        idx = 0
        while idx < len(tasks) or len(q) > 0:
            if len(q) > 0:
                v = heapq.heappop(q)
                r.append(v[1])
                t += v[0]

            if idx < len(tasks):
                if tasks[idx][0] > t and len(q) == 0:
                    t = tasks[idx][0]
                while idx < len(tasks) and tasks[idx][0] <= t:
                    heapq.heappush(q, (tasks[idx][1], tasks[idx][2]))
                    idx += 1


        return r        
