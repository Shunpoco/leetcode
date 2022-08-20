import heapq
from typing import List

class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        pq = []
        count = 0
        while len(stations) > 0 and (startFuel >= stations[0][0] or len(pq) > 0) and startFuel < target:
            while len(stations) > 0 and startFuel >= stations[0][0]:
                heapq.heappush(pq, -stations[0][1])
                stations.pop(0)

            f = -heapq.heappop(pq)
            startFuel += f
            count += 1
            
        while startFuel < target and len(pq) > 0:
            f = -heapq.heappop(pq)
            startFuel += f
            count += 1
            
        if startFuel < target:
            return -1
        
        return count
