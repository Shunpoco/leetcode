from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        rotate_list = []
        for col in range(n):
            temp = []
            for row in range(n):
                temp.insert(0, matrix[row][col])
            rotate_list.append(temp)

        for row in range(n):
            matrix[row] = rotate_list[row]

