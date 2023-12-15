class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        d = paths[0][1]

        while self.find(d, paths) >= 0:
            n = self.find(d, paths)

            d = paths[n][1]

        return d

    def find(self, a: str, paths)-> int:
        for i, path in enumerate(paths):
            if path[0] == a:
                return i

        return -1
