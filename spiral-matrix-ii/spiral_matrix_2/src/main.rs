struct Solution;
impl Solution {
    pub fn generate_matrix(n: i32) -> Vec<Vec<i32>> {
        let mut mat = vec![vec![0;n as usize];n as usize];
        let goal = n*n;
        let n = n as usize;
        let mut val = 1i32;
        let mut i = 0usize;
        while val <= goal {
            let outer = n as usize - 2 * i;
            let on = if outer == 1 { val } else { ((outer-1) as i32 * 4) + val -1 };
            let mut row = i;
            let mut col = i;
            while val <= on {
                mat[row][col] = val;
                val += 1;
                if col < n-1-i && row == i {
                    col += 1;
                } else if col > i && row == n-1-i {
                    col -= 1;
                } else if col == n-1-i && row < n-1-i {
                    row += 1;
                } else if col == i && row > i+1 {
                    row -= 1;
                }
            }

            i += 1;
        }
        println!("{:?}", mat);
        mat
    }
}

fn main() {
    assert_eq!(Solution::generate_matrix(3), vec![vec![1,2,3], vec![8,9,4], vec![7,6,5]]);
}
