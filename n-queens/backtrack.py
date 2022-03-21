class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        return self.backtrack(n, 0, [], [])
        
    
    def backtrack(self, n: int, row=0, prev=[], result=[]) -> List[List[str]]:
        for i in range(n):
            if self.check(i, prev):
                prev.append(i)
                if len(prev) == n:
                    result.append(self.convert(prev))
                else:
                    self.backtrack(n, row+1, prev, result)
                prev.pop()
                
        return result
    
    
    def check(self, col: int, prev: List[int]) -> bool:
        
        idx = len(prev)
        for i in range(len(prev)):
            if col == prev[i] or col-(idx-i) == prev[i] or col+(idx-i) == prev[i]:
                return False
            
        return True



    def convert(self, c: List[int]) -> List[str]:
        result = []
        for idx in c:
            t = ["."]*len(c)
            t[idx] = "Q"
            result.append("".join(t))
            
        return result
