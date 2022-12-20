from typing import List

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = [0 for _ in range(n)]
        queue = [0]
        visited[0] = 1

        while len(queue) > 0:
            room = queue.pop(0)
            keys = rooms[room]
            for key in keys:
                if visited[key] == 0:
                    queue.append(key)
                    visited[key] = 1
        
        return sum(visited) == n
