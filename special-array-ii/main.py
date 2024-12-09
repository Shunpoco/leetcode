class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        n = len(nums)

        parity = []

        for i in range(n-1):
            if (nums[i]%2) == (nums[i+1]%2):
                parity.append(i+1)

        result = []

        for query in queries:
            if self.search(query[0]+1, query[1], parity):
                result.append(False)
            else:
                result.append(True)

        return result


    def search(self, s, e, arr):
        l = 0
        r = len(arr)-1

        while l <= r:
            m = (l+r) // 2

            v = arr[m]

            if v < s:
                l = m + 1
            elif v > e:
                r = m - 1
            else:
                return True

        return False
