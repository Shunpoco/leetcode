class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums.sort()

        visited = [False for _ in range(len(nums))]
        result = -1
        for i in range(len(nums)):
            if visited[i]:
                continue

            num = nums[i]
            t = 0
            while self.find(num, 0, len(nums), nums) >= 0:
                visited[i] = True
                num **= 2
                t += 1

            if t >= 2 and t > result:
                result = t

        return result

    def find(self, v, s, e, nums) -> int:
        if s == e:
            return -1
        
        m = (s+e) // 2

        if nums[m] == v:
            return m

        if nums[m] > v:
            return self.find(v, s, m, nums)

        return self.find(v, m+1, e, nums)
