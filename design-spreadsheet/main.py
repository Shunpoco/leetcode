class Spreadsheet:

    def __init__(self, rows: int):
        self.sheet = [[0 for _ in range(26)] for _ in range(rows+1)]
        

    def setCell(self, cell: str, value: int) -> None:
        row, col = self.convert(cell)

        self.sheet[row][col] = value        

    def resetCell(self, cell: str) -> None:
        row, col = self.convert(cell)

        self.sheet[row][col] = 0

    def getValue(self, formula: str) -> int:
        formula = formula[1:]
        v = formula.split("+")

        v1 = 0
        try:
            v1 = int(v[0])
        except:
            row, col = self.convert(v[0])
            v1 = self.sheet[row][col]

        v2 = 0
        try:
            v2 = int(v[1])
        except:
            row, col = self.convert(v[1])
            v2 = self.sheet[row][col]

        return v1 + v2

    def col(self, s: str) -> int:
        if len(s) > 1:
            return -1

        return ord(s) - ord('A')
        

    def convert(self, s: str):
        if len(s) <= 1:
            return ()

        c = s[0]
        r = s[1:]

        col = self.col(c)
        row = int(r)

        return (row, col)


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)
