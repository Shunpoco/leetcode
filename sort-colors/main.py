class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        store = [0, 0, 0]
        
        for num in nums:
            store[num] += 1
            
        a = 0
        for i, s in enumerate(store):
            if i > 0:
                a += store[i-1]

            for j in range(a, s+a):
                nums[j] = i
