struct Solution;
impl Solution {
    pub fn lucky_numbers(matrix: Vec<Vec<i32>>) -> Vec<i32> {
        let n = matrix.len();
        let m = matrix[0].len();

        let mut max_col = vec![0; m];
        let mut min_row = vec![i32::MAX; n];

        for row in 0..n {
            for col in 0..m {
                let v = matrix[row][col];

                if v > max_col[col] {
                    max_col[col] = v;
                }

                if v < min_row[row] {
                    min_row[row] = v;
                }
            }
        }

        let mut result= vec![];
        for row in min_row.iter() {
            if max_col.contains(row) {
                result.push(*row);
            }
        }


        result
    }
}

fn main() {
    let matrix = vec![vec![3,7,8],vec![9,11,13],vec![15,16,17]];

    let got = Solution::lucky_numbers(matrix);

    println!("{:?}", got);
    assert_eq!(got, vec![15]);
}

#[cfg(test)]
mod test {
    use crate::Solution;

    #[test]
    fn case1() {
        let matrix = vec![vec![3,7,8],vec![9,11,13],vec![15,16,17]];

        let got = Solution::lucky_numbers(matrix);

        assert_eq!(got, vec![15]);
    }

    #[test]
    fn case2() {
        let matrix = vec![vec![1,10,4,2], vec![9,3,8,7], vec![15,16,17,12]];

        let got = Solution::lucky_numbers(matrix);

        assert_eq!(got, vec![12]);
    }

    #[test]
    fn case3() {
        let matrix = vec![vec![7, 8], vec![1, 2]];

        let got = Solution::lucky_numbers(matrix);

        assert_eq!(got, vec![7]);
    }
}
