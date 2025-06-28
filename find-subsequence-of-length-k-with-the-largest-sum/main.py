class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        mirror = [(num, i) for i, num in enumerate(nums)]
        mirror.sort(reverse=True)

        t = mirror[:k]
        tt = [(x[1], x[0]) for x in t]
        tt.sort()

        result = [x[1] for x in tt]

        return result



