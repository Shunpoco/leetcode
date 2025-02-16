class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        result = [0 for _ in range(n*2-1)]

        visited = [False for _ in range(n+1)]

        self.calc(0, result, visited, n)

        return result

    def calc(self, cur, result, visited, n):
        if cur == len(result):
            return True

        if result[cur] != 0:
            return self.calc(cur+1, result, visited, n)

        for i in range(n, 0, -1):
            if visited[i]:
                continue

            visited[i] = True
            result[cur] = i

            if i == 1:
                if self.calc(cur+1, result, visited, n):
                    return True

            elif cur+i < len(result) and result[cur+i] == 0:
                result[cur+i] = i

                if self.calc(cur+1, result, visited, n):
                    return True

                result[cur+i] = 0

            result[cur] = 0
            visited[i] = False

        return False

