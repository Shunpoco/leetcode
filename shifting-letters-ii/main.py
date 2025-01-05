class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        moves = [0 for _ in range(n)]
        for shift in shifts:
            if shift[2] == 1:
                moves[shift[0]] += 1
                if shift[1] + 1 < n:
                    moves[shift[1]+1] -= 1

            else:
                moves[shift[0]] -= 1
                if shift[1] + 1 < n:
                    moves[shift[1]+1] += 1

        result = list(s)
        nos = 0

        for i in range(n):
            nos = (nos + moves[i]) % 26
            if nos < 0:
                nos += 26

            c = chr(
                (ord(s[i]) - ord('a') + nos) % 26 + ord('a')
            )

            result[i] = c

        return ''.join(result)

