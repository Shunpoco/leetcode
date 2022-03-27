class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.cums = [0]
        t = 0
        for num in nums:
            t += num
            self.cums.append(t)
            
        print(self.cums)
        
        
    def sumRange(self, left: int, right: int) -> int:
        return self.cums[right+1] - self.cums[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
