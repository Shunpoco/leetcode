class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        
        former = self.countAndSay(n-1)
        
        result = ''
        cur = former[0]
        continuity = 0
        
        for idx in range(len(former)):
            if cur != former[idx]:
                result += str(continuity) + cur
                continuity = 0
            cur = former[idx]
            continuity += 1

        result += str(continuity) + cur
        
        return result
