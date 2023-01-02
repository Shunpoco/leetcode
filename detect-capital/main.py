class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        count_capital = 0

        for i, c in enumerate(word):
            if count_capital == 0 and ord(c) < 97:
                if i != 0:
                    return False
                count_capital += 1
            elif ord(c) < 97:
                count_capital += 1

        return count_capital <= 1 or count_capital == len(word)

