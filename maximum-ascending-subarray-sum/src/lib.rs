struct Solution;
impl Solution {
    pub fn max_ascending_sum(nums: Vec<i32>) -> i32 {
        let mut result = 0;

        let mut idx = 0;
        while idx < nums.len() {
            let mut cur = nums[idx];
            let mut t = cur;

            let mut j = idx + 1;
            while j < nums.len() && cur < nums[j] {
                cur = nums[j];
                t += cur;
                j += 1;
            }

            result = if t > result { t } else { result };
            idx = j;
        }

        result
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn one() {
        let nums = vec![10, 20, 30, 5, 10, 50];
        let result = Solution::max_ascending_sum(nums);

        assert_eq!(result, 65);
    }

    #[test]
    fn two() {
        let nums = vec![10, 20, 30, 40, 50];
        let result = Solution::max_ascending_sum(nums);

        assert_eq!(result, 150);
    }

    #[test]
    fn three() {
        let nums = vec![12, 17, 15, 13, 10, 11, 12];
        let result = Solution::max_ascending_sum(nums);

        assert_eq!(result, 33);
    }
}
