struct Solution {}

impl Solution {
    pub fn create_target_array(nums: Vec<i32>, index: Vec<i32>) -> Vec<i32> {
        let mut result = vec![];
        
        for i in 0..nums.len() {
            let mut num = nums[i];
            let idx = index[i] as usize;
            if idx < i {
                for j in idx..i {
                    let temp = result[j];
                    result[j] = num;
                    num = temp;
                }
            }
            result.push(num);
        }
        
        result
    }
}

fn main() {
    assert_eq!(Solution::create_target_array(vec![0,1,2,3,4], vec![0,1,2,2,1]), vec![0,4,1,3,2]);
}
