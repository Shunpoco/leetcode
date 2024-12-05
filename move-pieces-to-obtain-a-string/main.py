class Solution:
    def canChange(self, start: str, target: str) -> bool:
        idx = 0

        for i, c in enumerate(target):
            if c == 'L':
                if idx == len(start):
                    return False

                while idx < len(start):
                    if start[idx] == 'R':
                        return False
                    if start[idx] == '_':
                        idx += 1
                        if idx == len(start):
                            return False
                    else:
                        if idx < i:
                            return False
                        idx += 1
                        break

            elif c == 'R':
                if idx == len(start):
                    return False

                while idx < len(start):
                    if start[idx] == 'L':
                        return False
                    if start[idx] == '_':
                        idx += 1
                        if idx == len(start):
                            return False
                    else:
                        if idx > i:
                            return False
                        idx += 1
                        break

        while idx < len(start):
            if start[idx] != '_':
                return False
            idx += 1

        return True

