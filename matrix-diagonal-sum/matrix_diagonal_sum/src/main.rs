struct Solution {}

impl Solution {
    pub fn diagonal_sum(mat: Vec<Vec<i32>>) -> i32 {
        let l = mat.len();
        
        let mut primary = 0i32;
        let mut secondary = 0i32;
        
        for i in 0..l {
            primary += mat[i][i];
            secondary += mat[i][l-1-i];
        }
        
        if l % 2 != 0 {
            secondary -= mat[l/2][l/2];
        }
        
        primary + secondary
    }
}

fn main() {
    assert_eq!(Solution::diagonal_sum(vec![vec![1,2,3],vec![4,5,6],vec![7,8,9]]), 25);
}
