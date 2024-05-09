class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort()

        r = 0
        c = 0
        for i in range(k):
            v = happiness[len(happiness)-i-1]
            r += max(0, v-c)
            c += 1

        return r
