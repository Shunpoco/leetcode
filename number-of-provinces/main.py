from typing import List

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False for _ in range(n)]

        result = 0
        for i in range(n):
            if visited[i]:
                continue
            queue = [i]
            visited[i] = True
            result += 1

            while len(queue) > 0:
                v = queue.pop(0)

                for i, con in enumerate(isConnected[v]):
                    if con == 0 or visited[i]:
                        continue
                    queue.append(i)
                    visited[i] = True

        return result

