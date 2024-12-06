class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned.sort()

        result = 0

        for num in range(1, n+1):
            if self.search(banned, num):
                continue

            maxSum -= num
            if maxSum < 0:
                break

            result += 1

        return result

    def search(self, banned, num):
        l, r = 0, len(banned)-1

        while l <= r:
            m = (l+r) // 2
            if banned[m] == num:
                return True
            
            if banned[m] > num:
                r = m - 1
            else:
                l = m + 1

        return False

