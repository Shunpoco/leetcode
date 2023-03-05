from typing import List

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        paths = defaultdict(list)
        for idx, num in enumerate(arr):
            paths[num].append(idx)

        visited = [False for _ in range(n)]
        queue = [(0, 0)]
        visited[0] = True

        while len(queue) > 0:
            idx, steps = queue.pop(0)
            if idx == n-1:
                return steps
            for p in paths[arr[idx]]:
                if not visited[p]:
                    queue.append((p, steps+1))
                    visited[p] = True

            paths[arr[idx]] = []

            if idx - 1 >= 0 and not visited[idx-1]:
                queue.append((idx-1, steps+1))
                visited[idx-1] = True
            if idx + 1 < n and not visited[idx+1]:
                queue.append((idx+1, steps+1))
                visited[idx+1] = True

        
