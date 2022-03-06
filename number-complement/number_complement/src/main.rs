struct Solution;
impl Solution {
    pub fn find_complement(mut num: i32) -> i32 {
        let mut x = num;
        let mut y = 1;
        while x > 0 {
            num ^= y;
            y <<= 1;
            x >>= 1;
        }
        
        num
    }
}


fn main() {
    assert_eq!(Solution::find_complement(5), 2);
}
