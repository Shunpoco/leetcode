struct Solution;
impl Solution {
    pub fn hamming_distance(x: i32, y: i32) -> i32 {
        let mut diff = x^y;
        let mut count = 0i32;
        
        while diff > 0 {
            if diff&1 == 1 {
                count += 1;
            }
            diff >>= 1;
        }
        
        count
    }
}


fn main() {
    assert_eq!(Solution::hamming_distance(4, 1), 2);
}
