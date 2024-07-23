class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        dic = defaultdict(int)

        for num in nums:
            dic[num] += 1

        q = []
        for k, v in dic.items():
            q.append((v, -k))

        q.sort()

        result = []

        for num in q:
            for i in range(num[0]):
                result.append(-num[1])

        return result
    
