class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.sort(nums, 0, len(nums))

        return nums

    def sort(self, nums, left, right):
        if right-left == 1:
            return

        if right-left == 2:
            if nums[left] > nums[left+1]:
                t = nums[left]
                nums[left] = nums[left+1]
                nums[left+1] = t

            return

        m = (left+right) // 2

        self.sort(nums, left, m)
        self.sort(nums, m, right)

        q = []
        i = left
        j = m

        while i < m or j < right:
            if i == m:
                q.append(nums[j])
                j += 1
            elif j == right:
                q.append(nums[i])
                i += 1
            else:
                if nums[i] < nums[j]:
                    q.append(nums[i])
                    i += 1
                else:
                    q.append(nums[j])
                    j += 1
        for i in range(len(q)):
            nums[left+i] = q[i]

        return
