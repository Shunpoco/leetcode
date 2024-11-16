struct Solution;
impl Solution {
    pub fn results_array(nums: Vec<i32>, k: i32) -> Vec<i32> {
        let k = k as usize;
        
        if k == 1 {
            return nums;
        }

        let n = nums.len();
        let mut result = Vec::new();

        for i in 0..(n - k as usize + 1) {
            if i == 0 || result[i-1] == -1 {
                if Solution::is_consecutive(&nums[i..i+k]) {
                    result.push(nums[i+k-1]);
                } else {
                    result.push(-1);
                }
            } else {
                if nums[i+k-1] == nums[i+k-2] + 1 {
                    result.push(nums[i+k-1]);
                } else {
                    result.push(-1);
                }
            }
        }

        result
    }

    fn is_consecutive(nums: &[i32]) -> bool {
        let mut cur = nums[0];

        for i in 1..nums.len() {
            if nums[i] != cur + 1 {
                return false;
            }
            cur = nums[i];
        }

        true
    }
}

#[cfg(test)]
mod tests {
    use crate::Solution;

    #[test]
    fn case1() {
        let nums = vec![1, 2, 3, 4, 3, 2, 5];
        let k = 3;

        let got = Solution::results_array(nums, k);

        assert_eq!(got, vec![3, 4, -1, -1, -1]);
    }

    #[test]
    fn case2() {
        let nums = vec![2, 2, 2, 2, 2];
        let k = 4;

        let got = Solution::results_array(nums, k);

        assert_eq!(got, vec![-1, -1]);
    }

    #[test]
    fn case3() {
        let nums = vec![3, 2, 3, 2, 3, 2];
        let k = 2;

        let got = Solution::results_array(nums, k);

        assert_eq!(got, vec![-1, 3, -1, 3, -1]);
    }

    #[test]
    fn case4() {
        let nums = vec![1, 2, 3, 4];
        let k = 1;

        let got = Solution::results_array(nums, k);

        assert_eq!(got, vec![1, 2, 3, 4]);
    }
}
