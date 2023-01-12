from typing import List

class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        result = [0] * n
        tree = [[] for _ in range(n)]
        for a, b in edges:
            tree[a].append(b)
            tree[b].append(a)
        visited = [False for _ in range(n)]
        visited[0] = True

        self.execute(0, tree, labels, visited, result)
        return result


    def execute(self, n: int, tree: List[List[int]], labels: str, visited: List[int], result: List[int]) -> List[int]:
        memo = [0] * 26
        c = labels[n]
        memo[ord(c)-ord('a')] += 1

        for child in tree[n]:
            if not visited[child]:
                visited[child] = True
                m = self.execute(child, tree, labels, visited, result)
                memo = [a+b for a, b, in zip(memo, m)]

        result[n] = memo[ord(c)-ord('a')]
        return memo

