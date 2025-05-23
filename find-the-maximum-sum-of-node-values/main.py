class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        sums = 0
        count = 0
        positiveMin = 1 << 30
        negativeMax = -1 * (1 << 30)

        for num in nums:
            xor = num ^ k
            sums += num
            gain = xor - num
            if gain > 0:
                positiveMin = min(positiveMin, gain)
                sums += gain
                count += 1

            else:
                negativeMax = max(negativeMax, gain)

        if count %2 == 0:
            return sums

        return max(sums - positiveMin, sums + negativeMax)
