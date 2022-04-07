struct Solution;
impl Solution {
    pub fn matrix_reshape(mat: Vec<Vec<i32>>, r: i32, c: i32) -> Vec<Vec<i32>> {
        let elements = mat.len() * mat[0].len();
        
        if elements != (r*c) as usize {
            return mat;
        }
        
        let mut result = vec![];
        let mut t = vec![];
        for r_ in 0..mat.len() {
            for c_ in 0..mat[0].len() {
                println!("{:?}, {}", t, mat[r_][c_]);
                t.push(mat[r_][c_]);
                if t.len() == c as usize {
                    result.push(t.clone());
                    t = vec![];
                }
            }
        }
        
        result
    }
}


fn main() {
    assert_eq!(Solution::matrix_reshape(vec![vec![1,2], vec![3,4]], 1, 4), vec![vec![1,2,3,4]]);
}
