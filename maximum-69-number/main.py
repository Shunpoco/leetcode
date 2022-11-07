class Solution:
    def maximum69Number (self, num: int) -> int:
        result = num
        
        digit = 1
        t = num
        while digit < num:
            v = t % 10
            if v == 6:
                result = num - 6*digit + 9*digit
            
            digit *= 10
            t = t // 10
            
        return result
