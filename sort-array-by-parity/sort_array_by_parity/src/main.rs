struct Solution;
impl Solution {
    pub fn sort_array_by_parity(nums: Vec<i32>) -> Vec<i32> {
        let mut result = vec![-1;nums.len()];
        let mut even_idx = 0usize;
        let mut odd_idx = nums.len()-1;
        
        for &num in nums.iter() {
            if num%2 == 0 {
                result[even_idx] = num;
                even_idx += 1;
            } else {
                result[odd_idx] = num;
                odd_idx -= 1;
            }
        }
        
        result
    }
}


fn main() {
    assert_eq!(Solution::sort_array_by_parity(vec![3,1,2,4]), vec![2,4,1,3]);
}
