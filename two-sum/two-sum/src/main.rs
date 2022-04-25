use std::collections::HashMap;

struct Solution{}

// impl Solution {
//     pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
//         let mut h = HashMap::new();
        
//         for i in 0..nums.len() {
//             let v = nums[i];
//             if h.contains_key(&v) {
//                 return vec![h[&v] as i32, i as i32];
//             }
//             h.insert(target-nums[i], i);
//         }
//         vec![]
//     }
// }

// 2021-09-06
// impl Solution {
//     pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        
//         let mut h: HashMap<i32, i32> = HashMap::new();
        
//         for i in 0..nums.len() {
//             let v = nums[i];
//             match h.get(&v) {
//                 Some(val) => return vec![*val, i as i32],
//                 None => {
//                     h.insert(target-v, (i as i32));
//                 }
//             }
//         }
        
//         vec![]
//     }
// }

// 2022-04-26
impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut result = vec![];
        let mut memory = HashMap::new();
        for i in 0..nums.len() {
            if let Some(v) = memory.get(&nums[i]) {
                result.push(*v);
                result.push(i as i32);
                return result;
            }
            
            let v = target - nums[i];
            memory.insert(v, i as i32);
        }
        
        result
    }
}


fn main() {
    Solution::two_sum(vec![3,3], 6);
}

#[test]
fn test_two_sum() {
    let result = Solution::two_sum(vec![0, 1, 2], 3);
    assert_eq!(vec![1,2], result)
}
