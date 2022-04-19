struct Solution;
impl Solution {
    pub fn get_sum(mut a: i32, mut b: i32) -> i32 {
        let mut result = 0i32;
        let mut c = 0i32;
        for i in 0..32 {
            let v1 = a&1;
            let v2 = b&1;
            
            let c_: i32;
            let v: i32;
            if v1 == 1 && v2 == 1 && c == 1 {
                c_ = 1;
                v = 1;
            } else if v1&v2 == 1 || v2&c == 1 || c&v1 == 1 {
                c_ = 1;
                v = 0;
            } else if v1 == 1 || v2 == 1 || c == 1 {
                c_ = 0;
                v = 1;
            } else {
                c_ = 0;
                v = 0;
            }
            
            c = c_;
            result ^= v<<i;
            
            a >>= 1;
            b >>= 1;
        }
        result        
    }
}

fn main() {
    assert_eq!(Solution::get_sum(1, 2), 3);
}
