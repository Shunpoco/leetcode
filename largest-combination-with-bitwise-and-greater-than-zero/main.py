class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        counter = [0 for _ in range(24)]

        for i in range(24):
            for num in candidates:
                if (num & (1 << i)) != 0:
                    counter[i] += 1

        return max(counter)

