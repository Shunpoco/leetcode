class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()

        result = []
        v = folder[0]

        for i in range(1, len(folder)):
            t = folder[i]

            if not self.isSub(v, t):
                result.append(v)
                v = t

        result.append(v)

        return result
    
    def isSub(self, a, b):
        return b[:len(a)] == a and (len(a) == len(b) or b[len(a)] == "/")
