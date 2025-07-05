class Solution:
    def findLucky(self, arr: List[int]) -> int:
        nums = [0 for _ in range(500)]

        for a in arr:
            nums[a-1] += 1

        result = -1
        for i in range(1, 501):
            if nums[i-1] == i:
                result = i

        return result

