pub struct Solution;
impl Solution {
    pub fn check_if_exist(mut arr: Vec<i32>) -> bool {
        arr.sort();

        for i in 0..arr.len() {
            let v = arr[i];
            if v * 2 > arr[arr.len()-1] {
                return false;
            }

            match arr.binary_search(&(v*2)) {
                Ok(r) => {
                    if r != i {
                        return true;
                    }
                },
                Err(_) => {},
            };
        }

        false
    }
}

#[cfg(test)]
mod tests {
    use crate::Solution;

    #[test]
    fn case1() {
        let arr = vec![10, 2, 5, 3];
        let got = Solution::check_if_exist(arr);

        assert!(got);
    }

    #[test]
    fn case2() {
        let arr = vec![3, 1, 7, 11];
        let got = Solution::check_if_exist(arr);

        assert!(!got);
    }

    #[test]
    fn case3() {
        let arr = vec![-2, 0, 10, -19, 4, 6, -8];
        let got = Solution::check_if_exist(arr);

        assert!(!got);
    }
}
