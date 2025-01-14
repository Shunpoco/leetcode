class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        na = max(A)
        nb = max(B)
        n = max(na, nb) + 1
        na = [0] * n
        nb = [0] * n

        result = [0] * len(A)
        for i in range(len(A)):
            na[A[i]] += 1
            nb[B[i]] += 1

            for j in range(n):
                result[i] += min(na[j], nb[j])

        return result

