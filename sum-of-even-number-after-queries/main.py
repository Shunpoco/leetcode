from typing import List

class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        result = []
        sum_ = 0
        for num in nums:
            if num%2 == 0:
                sum_ += num
                
        for query in queries:
            num = nums[query[1]]
            
            if num%2 == 0:
                sum_ -= num
            
            v = num + query[0]
            
            if v%2 == 0:
                sum_ += v
                
            result.append(sum_)
            nums[query[1]] = v
            
            
        return result
