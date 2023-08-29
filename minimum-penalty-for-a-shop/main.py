class Solution:
    def bestClosingTime(self, customers: str) -> int:
        cur = 0
        for c in customers:
            if c == "N":
                cur += 1

        max_p = cur
        idx = len(customers)
        for i in range(len(customers)-1, -1, -1):
            if customers[i] == "N":
                cur -= 1
            elif customers[i] == "Y":
                cur += 1

            if max_p >= cur:
                max_p = cur
                idx = i

        return idx
