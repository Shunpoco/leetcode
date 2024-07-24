class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        q = []

        for i, num in enumerate(nums):
            q.append((self.convert(mapping, num), i, num))

        q.sort()

        result = []
        for v in q:
            result.append(v[2])

        return result

    def convert(self, mapping, nums)-> int:
        if nums == 0:
            return mapping[nums]
        r = 0
        t = 1
        while nums > 0:
            v = nums % 10
            r += mapping[v] * t
            nums //= 10
            t *= 10

        return r
