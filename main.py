
class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        result = 0
        n = len(nums)

        for i in range(1, n-1):
            if nums[i] == nums[i-1]:
                continue
            l = 0
            for j in range(i-1, -1, -1):
                if nums[j] > nums[i]:
                    l = 1
                    break
                elif nums[j] < nums[i]:
                    l = -1
                    break
            
            r = 0
            for j in range(i+1, n):
                if nums[j] > nums[i]:
                    r = 1
                    break
                elif nums[j] < nums[i]:
                    r = -1
                    break

            if l == r and l != 0:
                result += 1

        return result


