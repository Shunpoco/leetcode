struct Solution;
impl Solution {
    pub fn num_trees(n: i32) -> i32 {        
        let mut memory = vec![-1;n as usize + 1];
        memory[0] = 1;
        memory[1] = 1; // 1
        Solution::num_(n, &mut memory)
    }
    
    fn num_(n: i32, memory: &mut Vec<i32>) -> i32 {
        if memory[n as usize] != -1 {
            return memory[n as usize];
        }

        let mut result = 0i32;
        
        for i in 0..n {
            result += Solution::num_(i, memory) * Solution::num_(n-1-i, memory);
        }
        
        memory[n as usize] = result;
        
        result
    }
}


fn main() {
    assert_eq!(Solution::num_trees(3), 5);
}
