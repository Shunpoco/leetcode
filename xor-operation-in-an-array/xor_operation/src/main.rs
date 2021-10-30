struct Solution {}

impl Solution {
    pub fn xor_operation(n: i32, start: i32) -> i32 {
        let mut result = 0i32;
        
        for i in 0..n {
            let v = start + 2*i;
            
            result = result ^ v;
        }
        
        result
    }
}

fn main() {
    assert_eq!(Solution::xor_operation(5, 0), 8);
}

