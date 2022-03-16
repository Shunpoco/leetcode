struct Solution;
impl Solution {
    pub fn set_zeroes(matrix: &mut Vec<Vec<i32>>) {
        let mut zero_m = vec![];
        for i in 0..matrix.len() {
            for j in 0..matrix[0].len() {
                let v = matrix[i][j];
                if v == 0 {
                    zero_m.push(i);
                    break;
                }
            }
        }
        
        let mut zero_n = vec![];
        for i in 0..matrix[0].len() {
            for j in 0..matrix.len() {
                let v = matrix[j][i];
                if v == 0 {
                    zero_n.push(i);
                    break;
                }
            }
        }
        
        for &i in zero_m.iter() {
            matrix[i] = vec![0;matrix[0].len()];
        }
        
        for &i in zero_n.iter() {
            for j in 0..matrix.len() {
                matrix[j][i] = 0;
            }
        }
    }
}


fn main() {
    let mut v = vec![vec![1,1,1],vec![1,0,1],vec![1,1,1]];
    Solution::set_zeroes(&mut v);
    assert_eq!(v, vec![vec![1,0,1],vec![0,0,0],vec![1,0,1]]);
}
