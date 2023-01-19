class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        t = 0
        cums = defaultdict(list)
        cums[0].append(0)
        for i, num in enumerate(nums):
            t += num
            t %= k
            cums[t].append(i+1)

        result = 0
        for _, v in cums.items():
            result += int(len(v)*(len(v)-1)/2)

        return result
