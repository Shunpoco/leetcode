struct Solution;
impl Solution {
    pub fn get_maximum_generated(n: i32) -> i32 {
        let mut max = 0i32;
        let mut mem = vec![0;(n+1) as usize];
        
        for i in 1..(n+1) as usize {
            if i == 1 {
                mem[i] = 1;
            } else if i%2 == 0 {
                mem[i] = mem[i/2];
            } else {
                mem[i] = mem[(i-1)/2] + mem[(i-1)/2+1];
            }
            
            if mem[i] > max {
                max = mem[i];
            }
        }
        
        max
    }
}

fn main() {
    assert_eq!(Solution::get_maximum_generated(7), 3);
}
