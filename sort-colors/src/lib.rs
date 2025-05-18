struct Solution;

impl Solution {
    pub fn sort_colors(nums: &mut Vec<i32>) {
        let mut memo = vec![0;3];

        for &num in nums.iter() {
            memo[num as usize] += 1;
        }

        let mut idx = 0;
        for i in 0..3 {
            let mut count = memo[i];
            while count > 0 {
                nums[idx] = i as i32;
                idx += 1;
                count -= 1;
            }
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn first() {
        let mut nums = vec![2, 0, 2, 1, 1, 0];
        Solution::sort_colors(&mut nums);

        assert_eq!(nums, vec![0, 0, 1, 1, 2, 2])
    }

    #[test]
    fn second() {
        let mut nums = vec![2, 0, 1];
        Solution::sort_colors(&mut nums);

        assert_eq!(nums, vec![0, 1, 2]);
    }
}
