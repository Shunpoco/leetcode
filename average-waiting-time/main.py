class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        total = 0

        now = 0
        for customer in customers:
            start = max(now, customer[0])
            end = start + customer[1]

            total += end - customer[0]
            now = end

        return total / len(customers)
