class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num < 2:
            return False

        r = set([1])
        
        n = 2
        while n*n <= num:
            if num%n == 0:
                r.add(n)
                r.add(num/n)
                
            n += 1
            
        return sum(r) == num
