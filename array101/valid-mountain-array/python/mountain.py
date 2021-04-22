from typing import List

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False

        increase = True
        current = arr[0]

        for i in range(1, len(arr)):
            if increase:
                if arr[i] == current:
                    return False
                if arr[i] > current:
                    current = arr[i]
                    continue
                if i == 1:
                    return False
                current = arr[i]
                increase = False
            else:
                if arr[i] >= current:
                    return False
                current = arr[i]

        if increase == False:
            return True

        return False

