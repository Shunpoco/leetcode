class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        if n > 3 * limit:
            return 0

        result = 0
        for i in range(max(n-2*limit, 0), min(limit, n)+1):
            # for j in range(max(n-i-limit, 0), min(limit, n-i)+1):
            #     result += 1

            # This line is extract the above for loop
            result += max(min(limit, n-i) - max(n-i-limit, 0)+1, 0)


        return result

