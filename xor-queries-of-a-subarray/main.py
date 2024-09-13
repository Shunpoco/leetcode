class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        cum = [0]
        t = 0
        for a in arr:
            t ^= a
            cum.append(t)

        result = []
        for q in queries:
            result.append(cum[q[1]+1]^cum[q[0]])

        return result
