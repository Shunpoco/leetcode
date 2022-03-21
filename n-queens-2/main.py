class Solution:
    def totalNQueens(self, n: int) -> int:
        return self.backtrack(n, [], 0)
    
    def backtrack(self, n: int, prev: List[int], count: int) -> int:
        for i in range(n):
            if self.validate(i, prev):
                prev.append(i)
                if len(prev) == n:
                    count += 1
                else:
                    count = self.backtrack(n, prev, count)
                prev.pop()
        
        return count
    
    def validate(self, col: int, prev: List[int]) -> bool:
        b = len(prev)
        
        for i in range(b):
            if col == prev[i] or col-(b-i) == prev[i] or col+(b-i) == prev[i]:
                return False
            
        return True
