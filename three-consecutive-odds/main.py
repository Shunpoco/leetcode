class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        leftOdd = 0
        rightOdd = 0

        while rightOdd < len(arr):
            if arr[rightOdd] % 2 != 0:
                rightOdd += 1

                if rightOdd - leftOdd == 3:
                    return True

            else:
                leftOdd = rightOdd + 1
                rightOdd = leftOdd

        return False
            

