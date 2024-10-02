class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        ar = list(set(arr.copy()))
        ar.sort()

        memo = {}
        for i, a in enumerate(ar):
            memo[a] = i + 1

        return [memo[a] for a in arr]
