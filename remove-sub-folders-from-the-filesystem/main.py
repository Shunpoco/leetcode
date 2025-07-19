from typing import List

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

def test1():
    folder = ["/a", "/a/b", "/c/d", "/c/d/e", "/c/f"]
    result  = Solution().removeSubfolders(folder)
    expected = ["/a", "/c/d", "/c/f"]

    assert result == expected

def test2():
    folder = ["/a", "/a/b/c", "/a/b/d"]
    result = Solution().removeSubfolders(folder)
    expected = ["/a"]

    assert result == expected

def main():
    test1()
    test2()

if __name__ == '__main__':
    main()
