use std::collections::BinaryHeap;

struct Solution;
impl Solution {
    pub fn top_k_frequent(mut nums: Vec<i32>, k: i32) -> Vec<i32> {
        nums.sort();
        
        let mut memory = BinaryHeap::new();
        
        let mut v = nums[0];
        let mut count = 1;
        for i in 1..nums.len() {
            let num = nums[i];
            if num == v {
                count += 1;
            } else {
                memory.push((count, v));
                count = 1;
                v = num;
            }
        }
        memory.push((count, v));        
        
        println!("{:?}", memory);
        
        let mut result = vec![];
        for _ in 0..k {
            let v = memory.pop().unwrap();
            result.push(v.1);
        }
        
        result
    }
}

fn main() {
    assert_eq!(Solution::top_k_frequent(vec![3,0,1,0], 1), vec![0]);
}
