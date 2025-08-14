class Solution:
    def largestGoodInteger(self, num: str) -> str:
        result = -1

        count = 0
        prev = 
        for c in num:
            if prev != c:
                count = 1
                prev = c
            else:
                count += 1

            if count == 3:
                v = int(c)
                if v > result:
                    result = v

        if result == -1:
            return 

        return f{result}{result}{result}

