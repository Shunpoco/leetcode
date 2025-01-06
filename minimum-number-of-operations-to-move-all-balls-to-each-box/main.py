class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)

        result = [0 for _ in range(n)]

        ball_l, ball_r = 0, 0
        move_l, move_r = 0, 0

        for i in range(n):
            result[i] += move_l
            ball_l += int(boxes[i])
            move_l += ball_l

            j = n - 1 - i
            result[j] += move_r
            ball_r += int(boxes[j])
            move_r += ball_r

        return result

