from typing import List

class Solution:
    def diffWaysToCompute(self, e: str) -> List[int]:
        print(e)
        res = []
        for i in range(len(e)):
            if e[i] == "+" or e[i] == "-" or e[i] == "*":
                a = e[0:i]
                b = e[i+1:]
                res_a = self.diffWaysToCompute(a)
                res_b = self.diffWaysToCompute(b)
                
                for a_ in res_a:
                    for b_ in res_b:
                        if e[i] == "+":
                            res.append(a_+b_)
                        elif e[i] == "-":
                            res.append(a_-b_)
                        else:
                            res.append(a_*b_)
                            
        if len(res) == 0:
            res.append(int(e))
            
        return res
