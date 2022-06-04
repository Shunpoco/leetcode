class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cur = []
        for i in range(n):
            cur.append(["."]*n)

        res = []
        self.bt(0, n, cur, res)
        
        return res
        
        
    def bt(self, r: int, n: int, cur: List[List[str]], res: List[List[str]])-> bool:
        if r == n:
            r = []
            for item in cur:
                r.append("".join(item))
            
            res.append(r)
            return True
        
        for i in range(n):
            if self.check(r, i, cur):
                cur[r][i] = "Q"
                self.bt(r+1, n, cur, res)
                cur[r][i] = "."
                
        return False
    
    def check(self, r: int, c: int, cur: List[List[str]])-> bool:
        for i in range(r):
            if cur[i][c] == "Q":
                return False
            if c-(r-i) >= 0 and cur[i][c-(r-i)] == "Q":
                return False
            if c+(r-i) < len(cur) and cur[i][c+(r-i)] == "Q":
                return False
            
        return True
        
