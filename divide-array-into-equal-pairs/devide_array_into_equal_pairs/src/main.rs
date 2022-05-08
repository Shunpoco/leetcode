struct Solution;
impl Solution {
    pub fn divide_array(nums: Vec<i32>) -> bool {
        let mut mem = vec![0;501];
        for &num in nums.iter() {
            mem[num as usize] ^= 1;
        }
        
        mem.iter().sum::<i32>() == 0
    }
}

fn main() {
    assert_eq!(Solution::divide_array(vec![1,2,3,4]), false);
}
