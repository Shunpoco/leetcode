class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        inc = True
        dec = True
        prev = nums[0]


        for i in range(1, len(nums)):
            v = nums[i]
            if prev == v:
                inc &= True
                dec &= True
            elif prev < v:
                inc &= True
                dec &= False
            else:
                inc &= False
                dec &= True
            prev = v

        return inc | dec
