from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = ["+", "-", "*", "/"]

        for token in tokens:
            if token in operations:
                v1 = stack.pop()
                v2 = stack.pop()
                if token == "+":
                    stack.append(v2+v1)
                elif token == "-":
                    stack.append(v2-v1)
                elif token == "*":
                    stack.append(v2*v1)
                else:
                    sing = 1
                    if v1 < 0:
                        sing *= -1
                        v1 *= -1
                    if v2 < 0:
                        sing *= -1
                        v2 *= -1
                    stack.append(v2//v1 * sing)
            else:
                stack.append(self.toNum(token))

        return stack[0]            

    def toNum(self, token: str) -> int:
        r = 0
        positive = True
        for t in token:
            r *= 10
            if t == "-":
                positive = False
            else:
                r += int(t)

        if not positive:
            r *= -1
        return r
