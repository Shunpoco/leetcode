struct Solution;
impl Solution {
    pub fn search_matrix(matrix: Vec<Vec<i32>>, target: i32) -> bool {
        let m = matrix.len();
        let n = matrix[0].len();
        let mut v: &[i32] = &[0];
        for i in 0..m {
            if matrix[i][0] <= target && matrix[i][n-1] >= target {
                v = &matrix[i][..];
                break;
            }
            if i == m-1 {
                return false;
            }
        }
        
        while v.len() > 0 {
            let d = v.len() / 2;
            if v[d] == target {
                return true;
            }
            
            if v[d] < target {
                v = &v[d+1..];
            } else {
                v = &v[..d];
            }
        }
        
        false
    }
}


fn main() {
    assert_eq!(Solution::search_matrix(vec![vec![1,3,5,7], vec![10,11,16,20], vec![23,30,34,60]], 13), false);
}
