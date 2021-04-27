from typing import List

class Solution:
    def __init__(self):
        self.MIN = -2 ** 31 - 1
    def thirdMax(self, nums: List[int]) -> int:
        first = self.MIN
        second = self.MIN
        third = self.MIN

        for num in nums:
            if num >= first:
                if num == first:
                    continue
                t = first
                first = num
                num = t
            if num >= second:
                if num == second:
                    continue
                t = second
                second = num
                num = t
            if num > third:
                third = num
                continue

        if third == self.MIN:
            third = first

        return third
