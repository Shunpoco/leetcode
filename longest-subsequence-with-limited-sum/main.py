from typing import List

class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        result = [0 for _ in range(len(queries))]

        for i, query in enumerate(queries):
            r = 0
            for num in nums:
                if query >= num:
                    query -= num
                    r += 1
                else:
                    break

            result[i] = r
        return result
