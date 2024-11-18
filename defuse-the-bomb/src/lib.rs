struct Solution;
impl Solution {
    pub fn decrypt(code: Vec<i32>, k: i32) -> Vec<i32> {
        let n = code.len();

        let mut result = vec![0; n];

        if k == 0 {
            return result;
        }

        if k > 0 {
            let k = k as usize;
            for i in 0..n {
                let mut t = 0;
                for j in 1..k+1 {
                    t += code[(i+j)%n];
                }
                result[i] = t;
            }
        } else {
            let k = -k;
            for i in 0..n {
                let mut t = 0;
                for j in 1..k+1 {
                    let diff = ((n as i32 + (i as i32) - j) % (n as i32)) as usize;
                    t += code[diff];
                }
                result[i] = t;
            }
        }
        result
    }
}

#[cfg(test)]
mod tests {
    use crate::Solution;

    #[test]
    fn case1() {
        let code = vec![5, 7, 1, 4];
        let k = 3;

        let got = Solution::decrypt(code, k);

        assert_eq!(got, vec![12, 10, 16, 13]);
    }

    #[test]
    fn case2() {
        let code = vec![1, 2, 3, 4];
        let k = 0;

        let got = Solution::decrypt(code, k);

        assert_eq!(got, vec![0;4]);
    }

    #[test]
    fn case3() {
        let code = vec![2, 4, 9, 3];
        let k = -2;

        let got = Solution::decrypt(code, k);

        assert_eq!(got, vec![12, 5, 6, 13]);
    }
}
