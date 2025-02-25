class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        mod = 10 ** 9 + 7

        result = 0
        psum = 0
        oc = 0
        ec = 1

        for a in arr:
            psum += a
            if psum % 2 == 0:
                result += oc
                ec += 1
            else:
                result += ec
                oc += 1
            
            result %= mod

        return result

