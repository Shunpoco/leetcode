from typing import List, Tuple

from collections import defaultdict

class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        dim = len(img1)
        
        def non_zero_cells(img: List[List[int]]) -> List[Tuple[int]]:
            ret = []
            for x in range(dim):
                for y in range(dim):
                    if img[x][y] == 1:
                        ret.append((x, y))
                        
            return ret
                
        t_count = defaultdict(int)
        max_overlaps = 0
        
        ones1 = non_zero_cells(img1)
        ones2 = non_zero_cells(img2)
        
        for (x_a, y_a) in ones1:
            for (x_b, y_b) in ones2:
                vec = (x_b - x_a, y_b - y_a)
                t_count[vec] += 1
                max_overlaps = max(max_overlaps, t_count[vec])
                
        return max_overlaps
