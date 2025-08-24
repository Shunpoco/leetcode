class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        sums = []

        t = 0
        for num in nums:
            if num == 0:
                if t > 0:
                    sums.append(t)
                sums.append(0)
                t = 0
            else:
                t += 1

        sums.append(t)

        if len(sums) == 1:
            return max(0, sums[0]-1)

        result = 0
        for i in range(len(sums)):
            if i > 0 and i < len(sums)-1 and sums[i] == 0:
                result = max(result, sums[i-1] + sums[i+1])
            else:
                result = max(result, sums[i])
        
        return result

