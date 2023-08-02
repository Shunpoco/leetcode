from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)

        visited = [False for _ in range(n)]
        result = []
        v = []
        def calc():
            if len(v) == n:
                result.append(v.copy())
                return

            for i, num in enumerate(nums):
                if visited[i] == False:
                    visited[i] = True
                    v.append(num)
                    calc()
                    v.pop(-1)
                    visited[i] = False

        calc()

        return result
