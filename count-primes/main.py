class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 1:
            return 0
        
        primes = [True]*n
        primes[0] = False
        primes[1] = False
        idx = 2
        result = []
        while idx*idx < n:
            if primes[idx]:
                result.append(idx)
                v = 1
                while idx*v < n:
                    primes[idx*v] = False
                    v += 1
                
            idx += 1
        
        for (i, p) in enumerate(primes):
            if p:
                result.append(i)
        
        print(result)
        
        return len(result)
