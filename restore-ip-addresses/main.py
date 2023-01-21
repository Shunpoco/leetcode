from typing import List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []

        self.execute(0, s, "", 0, result)

        return result


    def execute(self, idx: int, s: str, ip: str, block: int, result: List[str]):
        if idx == len(s) and block == 4:
            result.append(ip[:len(ip)-1])
            return
        elif block >= 4:
            return

        for i in range(1, 4):
            v = s[idx:idx+i]
            if self.isValid(v):
                ip += v + '.'
                self.execute(idx+i, s, ip, block+1, result)
                ip = ip[:len(ip)-(len(v)+1)]



    def isValid(self, s: str) -> bool:
        if len(s) == 0 or len(s) > 3:
            return False

        if len(s) > 1 and s[0] == '0':
            return False

        if int(s) > 255:
            return False

        return True
