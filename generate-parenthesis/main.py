class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        
        self.solve(n, n, "", result)
        
        return result
    
    def solve(self, left, right, result, results):
        if left == 0 and right == 0:
            results.append(result)
            return
        
        if left > 0:
            self.solve(left-1, right, result+"(", results)
            
        if right > left:
            self.solve(left, right-1, result+")", results)
