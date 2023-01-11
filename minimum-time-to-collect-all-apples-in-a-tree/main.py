from typing import List, Tuple

class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        tree = [[] for _ in range(n)]
        for edge in edges:
            tree[edge[0]].append(edge[1])
            tree[edge[1]].append(edge[0])

        visited = [False for _ in range(n)]
        visited[0] = True
        return self.execute(0, tree, hasApple, visited)[0]

    def execute(self, n: int, tree: List[List[int]], hasApple: List[bool], visited: List[bool]) -> Tuple[int, bool]:
        apple = False
        if hasApple[n]:
            apple = True

        p = 0
        for nex in tree[n]:
            if not visited[nex]:
                visited[nex] = True
                v, has = self.execute(nex, tree, hasApple, visited)
                if has:
                    p += 2 + v
                    apple = True


        return p, apple
