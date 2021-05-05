class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        if N == 0:
            return 0

        odd = 0
        # indexが1からのため、奇数の場合はインクリメントが必要
        if K % 2 != 0:
            odd = 1
            K = K+1
        v = self.kthGrammar(N-1, int(K/2))

        # n-1の結果が0の場合、nでは01になりどちらかを取得
        if v == 0:
            if odd == 1:
                return 0
            else:
                return 1

        # n-1の結果が1の場合
        if odd == 1:
            return 1

        return 0

        
