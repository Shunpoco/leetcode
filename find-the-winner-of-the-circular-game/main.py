class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        q = [x+1 for x in range(n)]

        while len(q) > 1:
            for i in range(k):
                v = q.pop(0)
                if i < k-1:
                    q.append(v)

        return q[0]
