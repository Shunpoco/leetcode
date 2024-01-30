class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = ["+", "-", "*", "/"]

        for token in tokens:
            if token in operations:
                v1 = self.to_num(stack.pop(-1))
                v2 = self.to_num(stack.pop(-1))
                t = 0
                if token == "+":
                    t = v2 + v1
                elif token == "-":
                    t = v2 - v1
                elif token == "*":
                    t = v2 * v1
                else:
                    sing = 1
                    if v1 < 0:
                        sing *= -1
                        v1 *= -1
                    if v2 < 0:
                        sing *= -1
                        v2 *= -1
                    t = v2//v1 * sing
            
                stack.append(str(t))

            else:
                stack.append(token)

        return self.to_num(stack.pop(-1))


    def to_num(self, token: str) -> int:
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
