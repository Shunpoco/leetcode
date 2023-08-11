class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}

        self.calc(amount, coins, 0, memo)

        return memo[(amount, 0)]


    def calc(self, amount: int, coins: List[int], pos: int, memo: Dict[Tuple[int, int], int]):
        if memo.get((amount, pos)) is not None:
            return
        
        if amount == 0:
            memo[(amount, pos)] = 1
            return

        result = 0
        for i in range(pos, len(coins)):
            if amount - coins[i] >= 0:
                self.calc(amount-coins[i], coins, i, memo)
                result += memo[(amount-coins[i], i)]

        memo[(amount, pos)] = result
