from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        visited = [False for _ in range(len(nums))]
        queue = [0]
        visited[0] = True

        while len(queue) > 0:
            v = queue.pop(0)
            num = nums[v]
            if v == len(nums)-1 or v + num >= len(nums)-1:
                return True

            for i in range(1, num+1):
                if not visited[v+i]:
                    visited[v+i] = True
                    queue.append(v+i)

        return False
