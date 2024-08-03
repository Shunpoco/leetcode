class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        memo = defaultdict(int)

        for t in target:
            memo[t] += 1

        for a in arr:
            memo[a] -= 1

        for _, v in memo.items():
            if v != 0:
                return False

        return True
