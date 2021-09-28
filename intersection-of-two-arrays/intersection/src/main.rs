use std::collections::HashMap;

struct Solution {}

impl Solution {
    pub fn intersection(nums1: Vec<i32>, nums2: Vec<i32>) -> Vec<i32> {
        let mut h: HashMap<i32, i32> = HashMap::new();
        
        for num in nums1 {
            h.insert(num, 1);
        }
        
        let mut result: Vec<i32> = Vec::new();
        
        for num in nums2 {
            match h.get(&num) {
                Some(_v) => {
                    result.push(num);
                    h.remove(&num);
                },
                None => {
                    continue;
                }
            }
        }
        
        result
    }
}

fn main() {
    println!("{:?}", Solution::intersection(vec![1,2,1], vec![1]));
}
