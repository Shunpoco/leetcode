class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = "0"
        l = max(len(a), len(b))

        r = ''
        for i in range(l):
            a_ = a[len(a)-i-1] if len(a)-i-1 >= 0 else '0'
            b_ = b[len(b)-i-1] if len(b)-i-1 >= 0 else '0'

            if a_ == '1' and b_ == '1' and carry == '1':
                r = '1' + r
                carry = '1'
            elif a_ == '1' and b_ == '1' and carry == '0' or a_ == '1' and b_ == '0' and carry == '1' or a_ == '0' and b_ == '1' and carry == '1':
                r = '0' + r
                carry = '1'
            elif a_ == '1' or b_ == '1' or carry == '1':
                 r = '1' + r
                 carry = '0'
            else:
                r = '0' + r
                carry = '0'

        if carry == '1':
            r = '1' + r

        return r
