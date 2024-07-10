class Solution:
    def minOperations(self, logs: List[str]) -> int:
        p = 0

        for log in logs:
            if log == "../":
                p = max(p-1, 0)

            elif log != "./":
                p += 1

        return p
