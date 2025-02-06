class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        l = len(nums)

        pairs = []
        n_tuples = 0

        for i in range(l):
            for j in range(i+1, l):
                pairs.append(nums[i]*nums[j])

        pairs.sort()

        seen = -1
        count = 0

        for i in range(len(pairs)):
            if pairs[i] == seen:
                count += 1
            else:
                t = (count - 1) * count // 2
                n_tuples += 8 * t

                seen = pairs[i]
                count = 1

        t = (count - 1) * count // 2
        n_tuples += 8 * t

        return n_tuples
