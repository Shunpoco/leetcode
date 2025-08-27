class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        result = []

        self.calc([], turnedOn, result)

        return result

    def calc(self, cur: List[int], turnedOn: int, result: List[str]):
        if len(cur) == turnedOn:
            t = self.convert(cur)
            if t != "":
                result.append(t)
            return

        last = cur[-1] if len(cur) > 0 else -1

        for i in range(last+1, 10):
            cur.append(i)
            self.calc(cur, turnedOn, result)
            cur.pop()

    def convert(self, arr: List[int]) -> str:
        hour = 0
        minute = 0

        for n in arr:
            if n == 0:
                hour += 8
            elif n == 1:
                hour += 4
            elif n == 2:
                hour += 2
            elif n == 3:
                hour += 1
            elif n == 4:
                minute += 32
            elif n == 5:
                minute += 16
            elif n == 6:
                minute += 8
            elif n == 7:
                minute += 4
            elif n == 8:
                minute += 2
            else:
                minute += 1
            
        if hour < 12 and minute < 60:
            return f"{hour}:{ '0' if minute < 10 else '' }{minute}"

        return ""
