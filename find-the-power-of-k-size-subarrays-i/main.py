class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums
        
        n = len(nums)
        
        result = []

        for i in range(n-k+1):
            if i == 0 or result[i-1] == -1:
                if self.isConsecutive(nums[i:i+k]):
                    result.append(nums[i+k-1])
                else:
                    result.append(-1)

            else:
                t = nums[i:i+k]

                if t[-1] == t[-2] + 1:
                    result.append(t[-1])
                else:
                    result.append(-1)

        return result

    def isConsecutive(self, nums) -> bool:
        cur = nums[0]

        for i in range(1, len(nums)):
            if nums[i] != cur + 1:
                return False

            cur = nums[i]

        return True

