class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        
        formerS = self.countAndSay(n-1)
        
        result = ''
        currentC = formerS[0]
        continuity = 0
        
        for idx in range(len(formerS)):
            if currentC != formerS[idx]:
                result += str(continuity) + currentC
                continuity = 0
            currentC = formerS[idx]
            continuity += 1

        result += str(continuity) + currentC
        
        return result
