class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        memo = {
            5: 0,
            10: 0,
            20: 0,
        }

        for bill in bills:
            change = bill - 5
            if change != 0:
                if change == 5:
                    if memo[change] == 0:
                        return False
                    memo[change] -= 1
                elif change == 10:
                    if memo[change] == 0 and memo[5] < 2:
                        return False
                    if memo[change] > 0:
                        memo[change] -= 1
                    elif memo[5] > 1:
                        memo[5] -= 2
                else:
                    if (memo[5] == 0 or memo[10] == 0) and memo[5] < 3:
                        return False
                    if memo[5] != 0 and memo[10] != 0:
                        memo[5] -= 1
                        memo[10] -= 1
                    elif memo[5] > 2:
                        memo[5] -= 3

            memo[bill] += 1

        return True

