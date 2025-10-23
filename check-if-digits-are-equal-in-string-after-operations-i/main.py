
class Solution:
    def hasSameDigits(self, s: str) -> bool:
        nums = [int(x) for x in s]
        
        while len(nums) > 2:
            r = []
            for i in range(len(nums)-1):
                r.append((nums[i]+nums[i+1])%10)

            nums = r

        return nums[0] == nums[-1]


