class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        n = len(queries)
        result = []

        memo_b = {}
        memo_c = {}

        for i in range(n):
            b, c = queries[i]

            if b in memo_b:
                prev_c = memo_b[b]
                memo_c[prev_c] -= 1

                if memo_c[prev_c] == 0:
                    del memo_c[prev_c]

            memo_b[b] = c

            memo_c[c] = memo_c.get(c, 0) + 1

            result.append(len(memo_c))

        return result

