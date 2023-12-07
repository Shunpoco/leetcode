class Solution:
    def largestOddNumber(self, num: str) -> str:
        result = ""

        for i in range(len(num)-1, -1, -1):
            if num[i] in ['1', '3', '5', '7', '9']:
                result = num[:i+1]
                break

        return result
