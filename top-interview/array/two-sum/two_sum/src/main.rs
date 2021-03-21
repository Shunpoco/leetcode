struct Solution {}

impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        use std::collections::HashMap;

        let mut hm: HashMap<i32, i32> = HashMap::new();

        for i in 0..nums.len() {
            match hm.get(&(target - nums[i])) {
                Some(&i2) => return vec![i as i32, i2],
                None => hm.insert(nums[i], i as i32),
            };
        }
        vec![]
    }
}

fn main() {
    Solution::two_sum(vec![1,2], 3);
}

#[cfg(test)]
mod test {
    use super::*;

    #[test]
    fn it_two_sum() {
        let result = Solution::two_sum(vec![1,2,3], 3);
        assert_eq!(vec![1,0], result);
    }
}
