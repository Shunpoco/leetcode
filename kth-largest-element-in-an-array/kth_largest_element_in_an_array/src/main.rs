use std::collections::BinaryHeap;

struct Solution;
impl Solution {
    pub fn find_kth_largest(nums: Vec<i32>, k: i32) -> i32 {
        let mut pq = BinaryHeap::new();
        for &num in nums.iter() {
            pq.push(num);
        }
        
        let mut count = 0;
        let mut result = 0;
        while count < k {
            result = pq.pop().unwrap();
            count += 1;
        }
        
        result        
    }
}

fn main() {
    assert_eq!(Solution::find_kth_largest(vec![1,2,3,4], 2), 3);
}
