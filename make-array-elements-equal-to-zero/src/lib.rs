struct Solution;
impl Solution {
    pub fn count_valid_selections(nums: Vec<i32>) -> i32 {
        let mut result = 0;
        for i in 0..nums.len() {
            if nums[i] == 0 {
                let ls:i32 = nums[..i].iter().sum();
                let rs:i32 = nums[i+1..].iter().sum();

                match (ls-rs).abs() {
                    0 => result += 2,
                    1 => result += 1,
                    _ => {},
                }
            }
        }

        result
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn first() {
        let nums = vec![1, 0, 2, 0, 3];

        let got = Solution::count_valid_selections(nums);

        assert_eq!(got, 2);
    }

    #[test]
    fn second() {
        let nums = vec![2, 3, 4, 0, 4, 1, 0];

        let got = Solution::count_valid_selections(nums);

        assert_eq!(got, 0);
    }
}
