class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        memo = {}
        for n in arr2:
            memo[n] = 0

        rest = []
        for n in arr1:
            if memo.get(n) is not None:
                memo[n] += 1

            else:
                rest.append(n)

        rest.sort()

        r = []
        for n in arr2:
            for _ in range(memo[n]):
                r.append(n)

        for n in rest:
            r.append(n)

        return r

