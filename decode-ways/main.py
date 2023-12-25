class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}
        self.solve(s, memo)

        return memo[s]

    def solve(self, s: str, memo):
        if memo.get(s) is not None:
            return
        if s == '':
            memo[s] = 1
            return
        
        result = 0
        if self.isValid(s[0]):
            self.solve(s[1:], memo)
            result += memo[s[1:]]

        if len(s) >= 2 and self.isValid(s[0:2]):
            self.solve(s[2:], memo)
            result += memo[s[2:]]

        memo[s] = result
        return

    def isValid(self, s: str) -> bool:
        if s[0] == '0':
            return False

        if len(s) == 1:
            return True
        else:
            if s[0] != '1' and s[0] != '2':
                return False
            elif s[0] == '2' and (s[1] in ('7', '8', '9')):
                return False
            else:
                return True
