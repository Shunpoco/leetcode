from typing import List

class Solution:

    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:

        x1, y1 = coordinates[0][0], coordinates[0][1]

        x2, y2 = coordinates[1][0], coordinates[1][1]



        x2x1 = x2 - x1

        y2y1 = y2 - y1

        y1x2 = y1*x2

        y2x1 = y2*x1



        for i in range(2, len(coordinates)):

            x, y = coordinates[i][0], coordinates[i][1]



            if y * x2x1 != y2y1 * x + y1x2 - y2x1:

                return False



        return True


