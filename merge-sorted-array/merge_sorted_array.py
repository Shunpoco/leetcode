from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(n):
            idx = self.binarySearch(nums2[i], nums1[:m+i], 0)
            temp = nums1[idx:]
            nums1[idx] = nums2[i]
            nums1[idx+1:m+n] = temp[:len(temp)-1]

    def binarySearch(self, n: int, nums: List[int], start: int) -> int:
        print(nums, start)
        if len(nums) == 0:
            return start

        mid = len(nums) // 2
        if nums[mid] == n:
            return start + mid
        if n < nums[mid]:
            return self.binarySearch(n, nums[0:mid], start)
        if n > nums[mid]:
            return self.binarySearch(n, nums[mid+1:len(nums)], start + mid + 1)


# pythonの場合、 nums1 = hogehgoe とすると新しくListが作成される = nums1が置き換わってしまいin-placeにならない
