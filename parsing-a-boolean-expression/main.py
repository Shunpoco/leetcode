class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        idx = [0]

        return self.calc(expression, idx)

    def calc(self, expr: str, idx: list) -> bool:
        cur = expr[idx[0]]
        idx[0] += 1

        if cur == 't':
            return True
        if cur == 'f':
            return False

        # NOT
        if cur == '!':
            # Skip (
            idx[0] += 1
            result = not self.calc(expr, idx)
            # Skip )
            idx[0] += 1
            return result

        # AND / OR
        vals = []
        # Skip (
        idx[0] += 1
        while expr[idx[0]] != ')':
            if expr[idx[0]] != ',':
                vals.append(self.calc(expr, idx))
            else:
                idx[0] += 1
        # Skip )
        idx[0] += 1

        if cur == '&':
            return all(vals)

        if cur == '|':
            return any(vals)

        # Unreachable
        return False
