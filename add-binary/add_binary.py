class Solution:
    def addBinary(self, a: str, b: str)-> str:
        lenm = max(len(a), len(b))

        # fill by 0 if string is shorter than lanm
        prefa = '0'*(lenm - len(a))
        a = prefa + a
        prefb = '0'*(lenm - len(b))
        b = prefb + b

        counter = [0] * (lenm + 1)
        for i in range(lenm):
            temp = a[lenm-1-i] + b[lenm-1-i]
            if temp == '00':
                counter[i] = counter[i] + 0
            elif temp == '01' or temp == '10':
                counter[i] = counter[i] + 1
            else:
                counter[i] = counter[i] + 2

            # fix digits
            if counter[i] > 1:
                counter[i+1] = counter[i+1] + 1
                counter[i] = counter[i] % 2
        
        res = ''
        for i in range(len(counter)):
            num = str(counter[len(counter)-1-i])
            if res == '' and num == '0':
                continue
            res = res + num

        if res == '':
            res = '0'
        return res
