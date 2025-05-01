from sortedcontainers import SortedList

class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        n = len(tasks)
        m = len(workers)

        tasks.sort()
        workers.sort()

        def check(mid):
            p = pills
            w = SortedList(workers[m-mid:])

            for i in range(mid-1, -1, -1):
                if w[-1] >= tasks[i]:
                    w.pop()
                else:
                    if p == 0:
                        return False

                    r = w.bisect_left(tasks[i]-strength)
                    if r == len(w):
                        return False
                    p -= 1
                    w.pop(r)

            return True

        left, right, result = 1, min(m, n), 0
        while left <= right:
            mid = (left+right) // 2
            if check(mid):
                result = mid
                left = mid + 1

            else:
                right = mid - 1

        return result


