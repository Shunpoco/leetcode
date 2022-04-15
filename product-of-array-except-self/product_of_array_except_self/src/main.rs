struct Solution;
impl Solution {
    pub fn product_except_self(nums: Vec<i32>) -> Vec<i32> {
        let mut result = vec![];
        
        let mut v = 1;
        for &num in nums.iter() {
            result.push(v);
            v *= num;
        }
        
        v = 1;
        for i in 0..nums.len() {
            result[nums.len()-1-i] *= v;
            v *= nums[nums.len()-1-i];
        }
        
        result
    }
}

fn main() {
    assert_eq!(Solution::product_except_self(vec![1,2,3,4]), vec![24,12,8,6]);
}
