struct Solution;
impl Solution {
    pub fn arrange_coins(n: i32) -> i32 {
        let m = n as i64 * 2;
        
        let mut x = 1i64;
        while x*(x+1) < m {
            x += 1;
        }
        
        if x*(x+1) == m {
            return x as i32;
        }
        
        (x-1) as i32
    }
}

fn main() {
    assert_eq!(Solution::arrange_coins(1804289383), 60070);
}
