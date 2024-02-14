class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = []
        neg = []

        for num in nums:
            if num < 0:
                neg.append(num)
            else:
                pos.append(num)

        result = []

        for i in range(len(nums) // 2):
            result.append(pos[i])
            result.append(neg[i])

        return result
