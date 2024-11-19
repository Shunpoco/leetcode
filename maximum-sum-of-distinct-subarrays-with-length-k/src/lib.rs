use std::collections::HashMap;

struct Solution;
impl Solution {
    pub fn maximum_subarray_sum(nums: Vec<i32>, k: i32) -> i64 {
        let k = k as usize;

        let mut hm = HashMap::new();
        let mut result = 0;

        let mut start = 0;
        let mut end = 0;
        let mut cur_sum = 0;

        while end < nums.len() {
            let cur = nums[end];

            let v = match hm.get(&cur) {
                Some(v) => *v,
                None => -1,
            };

            while start as i32 <= v || end - start + 1 > k {
                cur_sum -= nums[start] as i64;
                start += 1;
            }

            hm.insert(cur, end as i32);
            cur_sum += nums[end] as i64;

            if end - start + 1 == k {
                result = if cur_sum > result { cur_sum } else { result };
            }

            end += 1;
        }

        result
    }
}

#[cfg(test)]
mod tests {
    use crate::Solution;

    #[test]
    fn case1() {
        let nums = vec![1, 5, 4, 2, 9, 9, 9];
        let k = 3;

        let got = Solution::maximum_subarray_sum(nums, k);

        assert_eq!(got, 15);
    }

    #[test]
    fn case2() {
        let nums = vec![4, 4, 4];
        let k = 3;

        let got = Solution::maximum_subarray_sum(nums, k);

        assert_eq!(got, 0);
    }
}
