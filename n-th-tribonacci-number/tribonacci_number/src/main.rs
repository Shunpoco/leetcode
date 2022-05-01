struct Solution;
impl Solution {
    pub fn tribonacci(n: i32) -> i32 {
        let mut mem = vec![-1;n as usize+1];
        mem[0] = 0;
        
        tribonacci(n as usize, &mut mem)
    }
}

fn tribonacci(n: usize, mem: &mut Vec<i32>) -> i32 {
    if mem[n] != -1 {
        return mem[n];
    }
    let r: i32;
    
    if n == 1 || n == 2 {
        r = 1;
    } else {
        r = tribonacci(n-1, mem) + tribonacci(n-2, mem) + tribonacci(n-3, mem);
    }
    mem[n] = r;
    
    r
}

fn main() {
    assert_eq!(Solution::tribonacci(5), 7);
}
