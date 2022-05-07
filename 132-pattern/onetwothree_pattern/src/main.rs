struct Solution;
impl Solution {
    pub fn find132pattern(nums: Vec<i32>) -> bool {
        let l = nums.len();
        let mut stack = vec![];
        
        let mut s3 = i32::MIN;
        for i in 0..nums.len() {
            if nums[l-1-i] < s3 {
                return true;
            }
            
            while stack.len() > 0 && nums[l-1-i] > stack[stack.len()-1] {
                s3 = stack.pop().unwrap();
            }
            
            stack.push(nums[l-1-i]);
        }
        
        false
    }
}


fn main() {
    assert_eq!(Solution::find132pattern(vec![3,1,4,2]), true);
}
