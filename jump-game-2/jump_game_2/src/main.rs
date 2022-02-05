use std::collections::HashMap;

struct Solution;
impl Solution {
    pub fn jump(nums: Vec<i32>) -> i32 {
        let mut hash = HashMap::new();
        hash.insert(nums.len()-1, 0);

        Solution::dp(0, &nums, &mut hash)
    }
    
    fn dp(current: usize, nums: &Vec<i32>, hash: &mut HashMap<usize, i32>) -> i32 {
        match hash.get(&current) {
            Some(v) => {
                return *v;
            },
            None => {},
        }
        
        let num = nums[current];
        let mut steps = 100000;
        for i in 1..num+1 {
            let next = current + i as usize;
            if next >= nums.len() {
                break;
            }
            let v = 1 + Solution::dp(current+i as usize, nums, hash);
            if steps > v {
                steps = v;
            }                
        }
        
        hash.insert(current, steps);
        
        steps
    }
}

fn main() {
    assert_eq!(Solution::jump(vec![2,3,1,1,4]), 2);
}
