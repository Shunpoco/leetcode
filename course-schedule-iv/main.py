class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        memo = defaultdict(list)

        for p in prerequisites:
            memo[p[1]].append(p[0])

        result = [False for _ in range(len(queries))]
        for i, query in enumerate(queries):
            visited = [False for _ in range(numCourses)]
            q = [query[1]]
            visited[query[1]] = True
            while len(q) > 0:
                v = q.pop(0)

                t = False
                for nex in memo[v]:
                    if nex == query[0]:
                        result[i] = True
                        t = True
                        break
                    if not visited[nex]:
                        visited[nex] = True
                        q.append(nex)

                if t:
                    break
                    

        return result

