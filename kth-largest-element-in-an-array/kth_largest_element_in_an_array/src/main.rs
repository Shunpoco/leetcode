use std::collections::BinaryHeap;

struct Solution;
impl Solution {
    pub fn find_kth_largest(nums: Vec<i32>, k: i32) -> i32 {
        let mut bh = BinaryHeap::new();
        
        for &num in nums.iter() {
            bh.push(num);
        }
        
        for _ in 0..(k-1) {
            bh.pop();
        }
        
        return bh.pop().unwrap();
    }
}


fn main() {
    assert_eq!(Solution::find_kth_largest(vec![1,2,3,4], 2), 3);
}
