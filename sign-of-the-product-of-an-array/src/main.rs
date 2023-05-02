struct Solution;
impl Solution {
    pub fn array_sign(nums: Vec<i32>) -> i32 {
        let mut digit = 1;

        for &num in nums.iter() {
            if num == 0 {
                return 0;
            } else if num < 0 {
                digit *= -1;
            }
        }

        digit
    }
}

fn main() {
    println!("{}", Solution::array_sign(vec![1,-1]));
}
