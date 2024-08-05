class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        memo = defaultdict(int)

        for a in arr:
            memo[a] += 1

        c = 0
        for i, a in enumerate(arr):
            if memo[a] == 1:
                c += 1
                if c == k:
                    return a

        return ""
