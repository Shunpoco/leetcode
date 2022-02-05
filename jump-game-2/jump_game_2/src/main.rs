struct Solution;
impl Solution {
    pub fn jump(nums: Vec<i32>) -> i32 {
        let mut memory = vec![-1; nums.len()];
        memory[nums.len()-1] = 0;
        
        Solution::dp(0, &nums, &mut memory)
    }
    
    fn dp(current: usize, nums: &Vec<i32>, memory: &mut Vec<i32>) -> i32 {
        if memory[current] >= 0 {
            return memory[current];
        }
        
        let num = nums[current];
        let mut steps = 100000;
        for i in 1..num+1 {
            let next = current + i as usize;
            if next >= nums.len() {
                break;
            }
            let v = 1 + Solution::dp(current+i as usize, nums, memory);
            if steps > v {
                steps = v;
            }                
        }
        
        memory[current] = steps;
        
        steps
    }
}

fn main() {
    assert_eq!(Solution::jump(vec![2,3,1,1,4]), 2);
}
