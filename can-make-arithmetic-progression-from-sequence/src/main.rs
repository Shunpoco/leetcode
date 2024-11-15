struct Solution;
impl Solution {
    pub fn can_make_arithmetic_progression(mut arr: Vec<i32>) -> bool {
        arr.sort();

        let diff = arr[1] - arr[0];

        for i in 1..arr.len()-1 {
            if arr[i+1] - arr[i] != diff {
                return false;
            }
        }

        true
    }
}

fn main() {
    let arr = vec![3, 5, 1];

    let got = Solution::can_make_arithmetic_progression(arr);

    assert!(got);

    println!("{}", got);
}


#[cfg(test)]
mod test {
    use crate::Solution;

    #[test]
    fn case1() {
        let arr = vec![3, 5, 1];

        let got = Solution::can_make_arithmetic_progression(arr);

        assert!(got);
    }

    #[test]
    fn case2() {
        let arr = vec![1, 2, 4];

        let got = Solution::can_make_arithmetic_progression(arr);

        assert!(!got);
    }
}