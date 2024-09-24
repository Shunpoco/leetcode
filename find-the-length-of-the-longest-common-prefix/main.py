class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        memo = defaultdict(bool)

        for arr in arr1:
            while arr > 0:
                memo[arr] = True
                arr //= 10

        result = 0
        for arr in arr2:
            while arr > 0:
                if memo.get(arr) and arr > result:
                    result = arr

                arr //= 10

        count = 0
        while result > 0:
            count += 1
            result //= 10

        return count

