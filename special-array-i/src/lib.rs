struct Solution {}
impl Solution {
    pub fn is_array_special(nums: Vec<i32>) -> bool {
        for i in 0..nums.len()-1 {
            if nums[i] % 2 == nums[i+1] % 2 {
                return false;
            }
        }

        true
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn one() {
        let nums = vec![1];
        let result = Solution::is_array_special(nums);

        assert!(result);
    }

    #[test]
    fn two() {
        let nums = vec![2, 1, 4];
        let result = Solution::is_array_special(nums);

        assert!(result);
    }

    #[test]
    fn three() {
        let nums = vec![4, 3, 1, 6];
        let result = Solution::is_array_special(nums);

        assert!(!result);
    }
}
