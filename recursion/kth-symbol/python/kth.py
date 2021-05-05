class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        if N == 0:
            return 0

        odd = 0
        if K % 2 != 0:
            odd = 1
            K = K+1
        v = self.kthGrammar(N-1, int(K/2))

        if v == 0:
            if odd == 1:
                return 0
            else:
                return 1

        if odd == 1:
            return 1

        return 0

        
