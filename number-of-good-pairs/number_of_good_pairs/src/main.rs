use std::collections::HashMap;

struct Solution {}

impl Solution {
    pub fn num_identical_pairs(nums: Vec<i32>) -> i32 {
        let mut map: HashMap<i32, Vec<usize>> = HashMap::new();
        
        for i in 0..nums.len() {
            let num = nums[i];
            match map.get_mut(&num) {
                Some(v) => {
                    v.push(i);
                },
                None => {
                    map.insert(num, vec![i]);
                }
            }
        }
        
        let mut result = 0i32;
        
        for key in map.keys() {
            let v = map.get(key).unwrap();
            let len = v.len();
            if len < 2 {
                continue;
            }
            result += (len * (len-1) / 2) as i32;            
        }
        
        result
    }
}

fn main() {
    println!("{}", Solution::num_identical_pairs(vec![1,1,1,2,3,4,2]));
}
