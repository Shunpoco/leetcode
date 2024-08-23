class Solution:
    def fractionAddition(self, expressions: str) -> str:
        num = 0
        denom = 1

        i = 0
        while i < len(expressions):
            cur_num = 0
            cur_denom = 0

            is_negative = False

            if expressions[i] in ['+', '-']:
                if expressions[i] == '-':
                    is_negative = True
                i += 1

            # num
            while i < len(expressions) and expressions[i].isdigit():
                v = int(expressions[i])
                cur_num = cur_num * 10 + v
                i += 1

            if is_negative:
                cur_num *= -1

            # skip devisor ('/')
            i += 1

            # denom
            while i < len(expressions) and expressions[i].isdigit():
                v = int(expressions[i])
                cur_denom = cur_denom * 10 + v
                i += 1

            # add fractions
            num = num * cur_denom + cur_num * denom
            denom = denom * cur_denom

        # reduce fractions
        gcd = abs(self.find_gcd(num, denom))
        num //= gcd
        denom //= gcd

        return f"{num}/{denom}"

    def find_gcd(self, a, b):
        if a == 0:
            return b

        return self.find_gcd(b%a, a)
