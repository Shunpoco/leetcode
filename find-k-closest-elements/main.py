from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        closest, exact = self.binarySearch(x, arr, 0, len(arr))
        if not exact:
            v = x - arr[closest]
            if v < 0:
                v *= -1
            
            if closest - 1 >= 0:
                v2 = x - arr[closest-1]
                if v2 < 0:
                    v2 *= -1
                    
                if v2 < v:
                    closest = closest-1
                    
            if closest + 1 < len(arr):
                v2 = arr[closest+1] - x
                if v2 < 0:
                    v2 *= -1
                    
                if v2 < v:
                    closest = closest+1
            
        
        result = [arr[closest]]
        k -= 1
        
        left = closest - 1
        right = closest + 1
        
        while k > 0 and left >= 0 and right < len(arr):
            l_d = x - arr[left]
            r_d = arr[right] - x
            if l_d < 0:
                l_d *= -1
            if r_d < 0:
                r_d *= -1
                
            if l_d <= r_d:
                result.insert(0, arr[left])
                left -= 1
            else:
                result.append(arr[right])
                right += 1
            k -= 1
        
        while k > 0 and left >= 0:
            result.insert(0, arr[left])
            left -= 1
            k -= 1
        while k > 0 and right >= 0:
            result.append(arr[right])
            right += 1
            k -= 1
        
        return result
    
    
    def binarySearch(self, target: int, arr: List[int], left: int, right: int) -> Tuple[int, bool]:
        if left+1 == right:
            if arr[left] == target:
                return left, True
            else:
                return left, False
        
        m = int((left+right)/2)
        
        if arr[m] == target:
            return m, True
        
        elif arr[m] > target:
            return self.binarySearch(target, arr, left, m)
        
        return self.binarySearch(target, arr, m, right)
        
        
