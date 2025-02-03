struct Solution;
impl Solution {
    pub fn longest_monotonic_subarray(nums: Vec<i32>) -> i32 {
        let mut result = 1;

        // Check increasing
        for i in 0..nums.len() {
            let mut t = 1;
            let mut cur = nums[i];
            for j in i+1..nums.len() {
                if nums[j] > cur {
                    t += 1;
                    cur = nums[j];
                } else {
                    break;
                }
            }

            result = if t > result { t } else { result };
        }

        // Check decreasing
        for i in 0..nums.len() {
            let mut t = 1;
            let mut cur = nums[i];
            for j in i+1..nums.len() {
                if nums[j] < cur {
                    t += 1;
                    cur = nums[j];
                } else {
                    break;
                }
            }

            result = if t > result { t } else { result };
        }

        result
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn one() {
        let nums = vec![1, 4, 3, 3, 2];
        let result = Solution::longest_monotonic_subarray(nums);

        assert_eq!(result, 2);
    }

    #[test]
    fn two() {
        let nums = vec![3, 3, 3, 3];
        let result = Solution::longest_monotonic_subarray(nums);

        assert_eq!(result, 1);
    }

    #[test]
    fn three() {
        let nums = vec![3, 2, 1];
        let result = Solution::longest_monotonic_subarray(nums);

        assert_eq!(result, 3);
    }
}
