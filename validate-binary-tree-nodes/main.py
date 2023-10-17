from typing import List

class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        visited = [i for i in range(n)]
        vis = [False for _ in range(n)]
        for i in range(n):
            if visited[i] != i:
                continue
            q = [i]
            vis[i] = True
            while len(q) > 0:
                v = q.pop(0)

                if leftChild[v] >= 0:
                    if visited[leftChild[v]] != leftChild[v]:
                        return False
                    visited[leftChild[v]] = v
                    if not vis[leftChild[v]]:
                        q.append(leftChild[v])
                        vis[leftChild[v]] = True

                if rightChild[v] >= 0:
                    if visited[rightChild[v]] != rightChild[v]:
                        return False
                    visited[rightChild[v]] = v
                    if not vis[rightChild[v]]:
                        q.append(rightChild[v])
                        vis[rightChild[v]] = True
                
        tops = []
        for i, v in enumerate(visited):
            if i == v:
                tops.append(i)

        if len(tops) > 1:
            return False

        c = 0
        while len(tops) > 0:
            v = tops.pop(0)
            c += 1

            if leftChild[v] != -1:
                tops.append(leftChild[v])

            if rightChild[v] != -1:
                tops.append(rightChild[v])

        return c == n

