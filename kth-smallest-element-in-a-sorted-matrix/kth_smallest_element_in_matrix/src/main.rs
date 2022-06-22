use std::collections::BinaryHeap;

struct Solution;
impl Solution {
    pub fn kth_smallest(matrix: Vec<Vec<i32>>, k: i32) -> i32 {
        let n = matrix.len();
        let mut bp = BinaryHeap::new();
        for i in 0..n {
            for j in 0..n {
                bp.push(-matrix[i][j]);
            }
        }
        
        let mut result = 0i32;
        for _ in 0..k {
            result = -bp.pop().unwrap();
        }
        
        result
    }
}


fn main() {
    assert_eq!(Solution::kth_smallest(vec![vec![1,5,9],vec![10,11,13],vec![12,13,15]], 8), 13);
}
