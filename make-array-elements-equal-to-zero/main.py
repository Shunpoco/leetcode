class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        result = 0


        for i in range(len(nums)):
            if nums[i] == 0:
                rs = sum(nums[:i])
                ls = sum(nums[i+1:])

                if abs(rs-ls) == 0:
                    result += 2
                if abs(rs-ls) == 1:
                    result += 1
        
        return result

