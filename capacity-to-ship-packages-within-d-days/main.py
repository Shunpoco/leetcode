from typing import List

class Solution:

    def shipWithinDays(self, weights: List[int], days: int) -> int:

        l = max(weights)

        r = sum(weights)

        m = (r+l)//2

        result = r

        while l < r:

            c = 1

            v = 0

            ok = True

            for weight in weights:

                if v + weight > m:

                    c += 1

                    v = 0

                if c > days:

                    ok = False

                    break

                v += weight

            

            if ok:

                result = m

                r = m

            else:

                l = m+1

            m = (r+l)//2

        

        return result


