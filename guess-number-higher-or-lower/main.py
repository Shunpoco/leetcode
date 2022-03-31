# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        return self.exec(1, n)
    
    def exec(self, start: int, end: int) -> int:
        m = int((end+start)/2)
        
        v = guess(m)
        
        if v == 0:
            return m
        elif v == -1:
            return self.exec(start, m-1)
        else:
            return self.exec(m+1, end)
