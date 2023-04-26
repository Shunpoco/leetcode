struct Solution {}

impl Solution {
    pub fn split(mut num: i32) -> Vec<i32> {
        let mut result = vec![];
        while num > 0 {
            result.push(num%10);
            num /= 10;
        }

        result
    }

    pub fn add_digits(mut num: i32) -> i32 {
        while num >= 10 {
            let digits = Solution::split(num);
            num = digits.iter().sum::<i32>();
        }

        num
    }
}

fn main() {
    assert_eq!(Solution::add_digits(38), 2);
}

#[test]
fn test_add_digits() {
    assert_eq!(Solution::add_digits(38), 2);
    assert_eq!(Solution::add_digits(0), 0);
    assert_eq!(Solution::add_digits(4833), 9);
    assert_eq!(Solution::add_digits(4800), 3);
}
